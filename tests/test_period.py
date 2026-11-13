import csv
import datetime as dt
import pathlib
import timeit

import pandas as pd
import pytest

from efa import EFADay, Period, SettlementDay
from efa.helpers import helpers

UTC = dt.timezone.utc
HH = dt.timedelta(minutes=30)
FIXTURE = pathlib.Path(__file__).parent / "fixtures" / "elexon_settlement_periods.csv"

# clocks forward, summer (BST), clocks back, winter (GMT)
DAYS = [
    dt.date(2026, 3, 29),
    dt.date(2026, 7, 15),
    dt.date(2026, 10, 25),
    dt.date(2026, 11, 11),
]
# EFA days touching them: the clock change sits in EFA day D, and EFA D+1
# starts 23:00 local on the change day
EFA_DAYS = [d + dt.timedelta(days=k) for d in DAYS for k in (0, 1)]


def _elexon_rows():
    with open(FIXTURE) as f:
        lines = [line for line in f if not line.startswith("#")]
    return [
        (
            dt.date.fromisoformat(r["settlement_date"]),
            int(r["settlement_period"]),
            dt.datetime.fromisoformat(r["start_time"].replace("Z", "+00:00")),
        )
        for r in csv.DictReader(lines)
    ]


ELEXON = _elexon_rows()


def _legacy_efa_bounds(date):
    """EFADay bounds as efa 0.2.20 derived them, through the helpers."""
    prev = date - dt.timedelta(days=1)
    start = helpers.utc_from_sp(prev, helpers.max_sp(prev) - 1)
    end = helpers.utc_from_sp(date, helpers.max_sp(date) - 1)
    return start, end


def _every_half_hour(start, end):
    t = start
    while t < end:
        yield t
        t += HH


# --- Elexon's own pairing ----------------------------------------------------


def test_fixture_covers_each_day_whole():
    counts = {d: sum(1 for r in ELEXON if r[0] == d) for d in DAYS}
    assert list(counts.values()) == [46, 48, 50, 48]


@pytest.mark.parametrize("date, n, start_time", ELEXON)
def test_from_settlement_matches_elexon(date, n, start_time):
    assert Period.from_settlement(date, n).start_time == start_time


@pytest.mark.parametrize("date, n, start_time", ELEXON)
def test_settlement_pair_matches_elexon(date, n, start_time):
    p = Period(start_time)
    assert (p.settlement_date, p.settlement_period) == (date, n)
    assert p in SettlementDay(date)
    assert SettlementDay(date).index(p) == n


@pytest.mark.parametrize("date", DAYS)
def test_settlement_day_periods_match_elexon(date):
    expected = [r[2] for r in ELEXON if r[0] == date]
    day = SettlementDay(date)
    assert [p.start_time for p in day.periods] == expected
    assert day.max_period == len(expected)
    assert day.start_time == expected[0]
    assert day.end_time == expected[-1] + HH


# --- against the existing helpers (the 0.2.20 derivation) --------------------


@pytest.mark.parametrize("date", DAYS)
def test_settlement_matches_helpers(date):
    day = SettlementDay(date)
    assert day.max_period == helpers.max_sp(date)
    for p in day.periods:
        assert helpers.sp_from_timestamp(p.start_time) == (
            p.settlement_date,
            p.settlement_period,
        )
        assert helpers.utc_from_sp(date, p.settlement_period) == p.start_time


@pytest.mark.parametrize("date", EFA_DAYS)
def test_efa_bounds_match_legacy(date):
    start, end = _legacy_efa_bounds(date)
    day = EFADay(date)
    assert day.start_time == start
    assert day.end_time == end
    assert isinstance(day.start_time, pd.Timestamp)
    assert isinstance(day.end_time, pd.Timestamp)


@pytest.mark.parametrize("date", EFA_DAYS)
def test_efa_every_half_hour(date):
    start, end = _legacy_efa_bounds(date)
    day = EFADay(date)
    expected = list(_every_half_hour(start, end))
    assert [p.start_time for p in day.periods] == expected
    for n, t in enumerate(expected, start=1):
        p = Period(t)
        assert (p.efa_date, p.efa_period) == (date, n)
        assert p.efa_day == day
        assert Period.from_efa(date, n) == p
        assert EFADay.from_start_time(t) == day
        assert EFADay.from_start_time(t + dt.timedelta(minutes=29)) == day


@pytest.mark.parametrize(
    "date, max_period",
    [
        (dt.date(2026, 3, 29), 46),
        (dt.date(2026, 3, 30), 48),
        (dt.date(2026, 7, 15), 48),
        (dt.date(2026, 10, 25), 50),
        (dt.date(2026, 10, 26), 48),
        (dt.date(2026, 11, 11), 48),
    ],
)
def test_efa_max_period(date, max_period):
    assert EFADay(date).max_period == max_period
    assert EFADay(date).max_efa_sp == max_period


def test_clocks_back_last_two_half_hours_stay_on_their_efa_day():
    # GC-871: 22:00 and 22:30 London on 2026-10-25 are EFA periods 49 and 50
    # of EFA 2026-10-25, not the next day
    for n, t in [(49, "2026-10-25T22:00Z"), (50, "2026-10-25T22:30Z")]:
        p = Period(t)
        assert (p.efa_date, p.efa_period) == (dt.date(2026, 10, 25), n)
        assert (p.settlement_date, p.settlement_period) == (
            dt.date(2026, 10, 25),
            n - 2,
        )


# --- one identity across both calendars --------------------------------------


@pytest.mark.parametrize("date", EFA_DAYS)
def test_efa_period_1_is_settlement_penultimate_of_day_before(date):
    prev = SettlementDay(date - dt.timedelta(days=1))
    assert Period.from_efa(date, 1) == Period.from_settlement(
        prev.date, prev.max_period - 1
    )


def test_equal_periods_hash_equal_across_timezones():
    utc = Period(dt.datetime(2026, 10, 25, 1, 0, tzinfo=UTC))
    london = Period(utc.start_time.astimezone(pd.Timestamp(0, tz="Europe/London").tz))
    assert utc == london
    assert hash(utc) == hash(london)
    assert utc.start_time.tzinfo is UTC


def test_settlement_day_is_not_efa_day():
    assert SettlementDay("2026-11-11") != EFADay("2026-11-11")


# --- constructors -------------------------------------------------------------


def test_from_start_time_rejects_naive():
    with pytest.raises(TypeError):
        Period.from_start_time(dt.datetime(2026, 11, 11, 12, 0))


def test_from_start_time_rejects_off_boundary():
    with pytest.raises(ValueError):
        Period.from_start_time(dt.datetime(2026, 11, 11, 12, 15, tzinfo=UTC))


def test_containing_floors():
    t = dt.datetime(2026, 11, 11, 12, 59, 59, tzinfo=UTC)
    assert Period.containing(t) == Period("2026-11-11T12:30Z")


def test_containing_rejects_naive():
    with pytest.raises(TypeError):
        Period.containing(dt.datetime(2026, 11, 11, 12, 0))


def test_accepts_pandas_timestamp_returns_stdlib():
    p = Period(pd.Timestamp("2026-11-11 12:00", tz="UTC"))
    assert type(p.start_time) is dt.datetime


def test_repr_round_trips():
    p = Period("2026-10-25T23:00Z")
    assert repr(p) == "Period('2026-10-25T23:00Z')"
    assert eval(repr(p)) == p


def test_london_marks_repeated_hour():
    first = Period("2026-10-25T00:00Z").london
    second = Period("2026-10-25T01:00Z").london
    assert (first.hour, first.fold) == (1, 0)
    assert (second.hour, second.fold) == (1, 1)


# --- arithmetic and ordering ---------------------------------------------------


def test_arithmetic_crosses_days():
    p = Period.from_settlement("2026-10-25", 50)
    assert p + 1 == Period.from_settlement("2026-10-26", 1)
    assert 1 + p == p + 1
    assert (p + 1) - 1 == p
    assert (
        Period.from_settlement("2026-10-26", 1)
        - Period.from_settlement("2026-10-25", 1)
        == 50
    )


def test_arithmetic_rejects_timedelta():
    with pytest.raises(TypeError):
        Period("2026-11-11T12:00Z") + HH


def test_ordering():
    a, b = Period("2026-11-11T12:00Z"), Period("2026-11-11T12:30Z")
    assert a < b and sorted([b, a]) == [a, b]


# --- day relationship -----------------------------------------------------------


def test_index_raises_for_period_not_in_day():
    day = EFADay("2026-11-11")
    with pytest.raises(ValueError):
        day.index(Period.from_efa("2026-11-12", 1))


@pytest.mark.parametrize("n", [0, 49, 1.0])
def test_period_number_out_of_range_raises(n):
    with pytest.raises(ValueError):
        SettlementDay("2026-11-11").period(n)


def test_contains_rejects_non_period():
    with pytest.raises(TypeError):
        dt.datetime(2026, 11, 11, tzinfo=UTC) in SettlementDay("2026-11-11")


# --- deprecations ----------------------------------------------------------------


def test_efa_day_from_naive_start_time_warns():
    with pytest.warns(DeprecationWarning, match="naive"):
        day = EFADay.from_start_time(dt.datetime(2026, 11, 11, 23, 0))
    assert day == EFADay("2026-11-12")


def test_old_efa_sp_methods_warn_and_agree():
    day = EFADay("2026-10-25")
    with pytest.warns(DeprecationWarning):
        assert day.efa_sp_from_utc(pd.Timestamp("2026-10-25T22:30Z")) == 50
    with pytest.warns(DeprecationWarning):
        assert day.utc_from_efa_sp(50) == pd.Timestamp("2026-10-25T22:30Z")


# --- speed (GC-756): no worse than gc-api's EfaPeriods per row ------------------


class _EfaPeriods:
    """gc-api dispatch.EfaPeriods: day bounds once, number by arithmetic."""

    def __init__(self):
        self._start = self._end = self._date = None

    def __call__(self, t):
        if self._start is None or not (self._start <= t < self._end):
            day = EFADay.from_start_time(t)
            self._start, self._end, self._date = day.start_time, day.end_time, day.date
        return self._date, int((t - self._start) // HH) + 1


def test_period_per_row_no_slower_than_efa_periods():
    t0 = dt.datetime(2026, 10, 20, tzinfo=UTC)
    rows = [t0 + HH * i for i in range(48 * 14)]

    def baseline():
        f = _EfaPeriods()
        return [f(t) for t in rows]

    def period():
        return [(p.efa_date, p.efa_period) for p in map(Period, rows)]

    assert period() == baseline()
    base = min(timeit.repeat(baseline, number=5, repeat=5))
    new = min(timeit.repeat(period, number=5, repeat=5))
    # measured 2026-11-13: Period 2.3 us/row vs EfaPeriods 2.8; slack for noise
    assert new < base * 1.5
