"""One half hour, named on either calendar (GC-1096).

A half hour has four names: its start instant, its London time, its
settlement date and period, and its EFA date and period. `Period` is the
half hour itself, keyed on its start instant in UTC, so EFA period 1 of D and
settlement period 47 of D-1 are the same `Period`.

Days are intervals, not containers. `SettlementDay` and `EFADay` differ only
in when the day starts (00:00 London, and 23:00 London the evening before);
everything else lives on `_CalendarDay`. A period number is defined relative
to a day: `day.index(period)` and `day.period(n)` convert, and asking for the
number of a period the day does not contain raises.

Stdlib only: no pandas here.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from typing import Tuple, Union
from zoneinfo import ZoneInfo

LONDON = ZoneInfo("Europe/London")
UTC = dt.timezone.utc


def _to_utc(t: dt.datetime) -> dt.datetime:
    """`t` as a plain stdlib datetime in UTC. Raises on naive input."""
    if not isinstance(t, dt.datetime):
        raise TypeError(f"expected a tz-aware datetime, not {type(t).__name__}")
    if t.tzinfo is None or t.utcoffset() is None:
        raise TypeError(f"{t} is naive; pass a tz-aware datetime")
    u = t.astimezone(UTC)
    # rebuild so a pd.Timestamp (a datetime subclass) comes out as a datetime
    return dt.datetime(
        u.year, u.month, u.day, u.hour, u.minute, u.second, u.microsecond, UTC
    )


class _CalendarDay:
    """A day on one calendar: an interval of half hours, `[start, end)`.

    Subclasses set `date` and supply `_start_of(date)`, the UTC instant the
    day starts. Day lengths (46, 48 or 50 periods) fall out of the bounds.
    """

    # The one place the period length is defined. When settlement periods
    # shorten it becomes a property of the calendar and era, not of a Period.
    PERIOD = dt.timedelta(minutes=30)

    date: dt.date

    @classmethod
    def _start_of(cls, date: dt.date) -> dt.datetime:
        raise NotImplementedError

    @property
    def _start(self) -> dt.datetime:
        return self._start_of(self.date)

    @property
    def _end(self) -> dt.datetime:
        return self._start_of(self.date + dt.timedelta(days=1))

    @property
    def max_period(self) -> int:
        """How many periods the day has: 48, or 46 / 50 on clock-change days."""
        return (self._end - self._start) // self.PERIOD

    @property
    def periods(self) -> Tuple["Period", ...]:
        """Every period of the day, in order."""
        start = self._start
        return tuple(Period(start + self.PERIOD * i) for i in range(self.max_period))

    def __contains__(self, period: "Period") -> bool:
        if not isinstance(period, Period):
            raise TypeError(f"only a Period can be in a day, not {period!r}")
        return self._start <= period.start_time < self._end

    def index(self, period: "Period") -> int:
        """The 1-based number of `period` within this day."""
        if period not in self:
            raise ValueError(f"{period!r} is not in {self!r}")
        return (period.start_time - self._start) // self.PERIOD + 1

    def period(self, n: int) -> "Period":
        """Period number `n` of this day."""
        if not isinstance(n, int):
            raise ValueError(f"period number must be an integer, not {n!r}")
        last = self.max_period
        if not 1 <= n <= last:
            raise ValueError(
                f"period number for {self} must be an integer in range 1 to {last}."
            )
        return Period(self._start + self.PERIOD * (n - 1))


@dataclass(frozen=True, order=True)
class SettlementDay(_CalendarDay):
    """A settlement day: 00:00 to 24:00 Europe/London.

    BSC Section X-1: a Settlement Day is "the period from 00:00 hours to 24:00
    hours on each day", and a Settlement Period is "a period of 30 minutes
    beginning on the hour or the half-hour in each Settlement Day", numbered
    from 1 at 00:00 local time.
    """

    date: dt.date

    def __post_init__(self) -> None:
        if isinstance(self.date, str):
            object.__setattr__(
                self, "date", dt.datetime.strptime(self.date, "%Y-%m-%d").date()
            )
        elif isinstance(self.date, dt.datetime) or not isinstance(self.date, dt.date):
            raise TypeError(f"SettlementDay takes a date, not {self.date!r}")

    @classmethod
    def _start_of(cls, date: dt.date) -> dt.datetime:
        return dt.datetime.combine(date, dt.time(0), LONDON).astimezone(UTC)

    def __str__(self) -> str:
        return self.date.strftime("%Y-%m-%d")

    def __repr__(self) -> str:
        return f"SettlementDay('{self}')"

    def __add__(self, days: int) -> "SettlementDay":
        if not isinstance(days, int):
            raise TypeError("Only integer values can be added to a SettlementDay")
        return SettlementDay(self.date + dt.timedelta(days=days))

    def __sub__(self, days: int) -> "SettlementDay":
        if not isinstance(days, int):
            raise TypeError(
                "Only integer values can be subtracted from a SettlementDay"
            )
        return SettlementDay(self.date - dt.timedelta(days=days))

    @property
    def start_time(self) -> dt.datetime:
        """UTC start of the day: 00:00 London."""
        return self._start

    @property
    def end_time(self) -> dt.datetime:
        """UTC end of the day (exclusive): 00:00 London the next day."""
        return self._end


@dataclass(frozen=True, order=True)
class Period:
    """One half hour, identified by its UTC start instant.

    Build one from a start instant (`Period(t)` or `Period.from_start_time(t)`,
    strict), from any instant inside it (`Period.containing(t)`), or from a
    date and period number on either calendar (`from_settlement`,
    `from_efa`). Every name for the half hour is a property derived from
    `start_time`; nothing else is stored.
    """

    start_time: dt.datetime

    def __post_init__(self) -> None:
        t = self.start_time
        if isinstance(t, str):
            t = dt.datetime.fromisoformat(t.replace("Z", "+00:00"))
        u = _to_utc(t)
        if getattr(t, "nanosecond", 0) or u.second or u.microsecond or u.minute % 30:
            raise ValueError(
                f"{t} is not the start of a half hour; use Period.containing()"
            )
        object.__setattr__(self, "start_time", u)

    @classmethod
    def from_start_time(cls, start_time: Union[dt.datetime, str]) -> "Period":
        """The period starting at `start_time` (tz-aware, on :00 or :30)."""
        return cls(start_time)

    @classmethod
    def containing(cls, t: dt.datetime) -> "Period":
        """The period containing the instant `t` (tz-aware, any time)."""
        u = _to_utc(t)
        return cls(u.replace(minute=u.minute - u.minute % 30, second=0, microsecond=0))

    @classmethod
    def from_settlement(cls, date: Union[dt.date, str], n: int) -> "Period":
        """Settlement period `n` of settlement date `date`."""
        return SettlementDay(date).period(n)

    @classmethod
    def from_efa(cls, date: Union[dt.date, str], n: int) -> "Period":
        """EFA period `n` of EFA date `date`."""
        from efa.efaday import EFADay

        return EFADay(date).period(n)

    def __repr__(self) -> str:
        return f"Period('{self}')"

    def __str__(self) -> str:
        return self.start_time.strftime("%Y-%m-%dT%H:%MZ")

    def __add__(self, n: int) -> "Period":
        if not isinstance(n, int):
            return NotImplemented
        return Period(self.start_time + _CalendarDay.PERIOD * n)

    __radd__ = __add__

    def __sub__(self, other: Union[int, "Period"]):
        if isinstance(other, Period):
            return (self.start_time - other.start_time) // _CalendarDay.PERIOD
        if isinstance(other, int):
            return Period(self.start_time - _CalendarDay.PERIOD * other)
        return NotImplemented

    @property
    def london(self) -> dt.datetime:
        """The start in Europe/London time (`fold` marks the repeated hour)."""
        return self.start_time.astimezone(LONDON)

    @property
    def settlement_date(self) -> dt.date:
        return self.london.date()

    @property
    def settlement_day(self) -> SettlementDay:
        return SettlementDay(self.settlement_date)

    @property
    def settlement_period(self) -> int:
        start = SettlementDay._start_of(self.settlement_date)
        return (self.start_time - start) // _CalendarDay.PERIOD + 1

    @property
    def efa_date(self) -> dt.date:
        # the EFA day starts 23:00 London the evening before
        local = self.london
        if local.hour >= 23:
            return local.date() + dt.timedelta(days=1)
        return local.date()

    @property
    def efa_day(self):
        from efa.efaday import EFADay

        return EFADay(self.efa_date)

    @property
    def efa_period(self) -> int:
        from efa.efaday import EFADay

        start = EFADay._start_of(self.efa_date)
        return (self.start_time - start) // _CalendarDay.PERIOD + 1
