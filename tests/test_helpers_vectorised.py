import numpy as np
import pandas as pd
import pytest
import pytz

from efa import helpers


def test_is_short_day_true():
    dates = pd.DatetimeIndex(
        [
            "2019-03-31",
            "2020-03-29",
            "2021-03-28",
            "2022-03-27",
            "2023-03-26",
            "2024-03-31",
        ],
        name="date",
    )
    result = helpers.vectorised.is_short_day(dates)
    assert result.all()
    assert type(result) == np.ndarray


def test_is_short_day_false():
    dates = pd.DatetimeIndex(
        [
            "2020-03-31",
            "2021-03-29",
            "2022-03-28",
            "2023-03-27",
            "2024-03-26",
            "2025-03-31",
            "2020-10-25",
            "2021-10-31",
            "2022-10-30",
            "2023-10-29",
            "2024-10-27",
        ],
        name="date",
    )
    result = helpers.vectorised.is_short_day(dates)
    assert not result.any()
    assert type(result) == np.ndarray


def test_is_long_day_true():
    dates = pd.DatetimeIndex(
        [
            "2020-10-25",
            "2021-10-31",
            "2022-10-30",
            "2023-10-29",
            "2024-10-27",
        ],
        name="date",
    )
    result = helpers.vectorised.is_long_day(dates)
    assert result.all()


def test_is_long_day_false():
    dates = pd.DatetimeIndex(
        [
            "2021-10-25",
            "2022-10-31",
            "2023-10-30",
            "2024-10-29",
            "2025-10-27",
            "2019-03-31",
            "2020-03-29",
            "2021-03-28",
            "2022-03-27",
            "2023-03-26",
            "2024-03-31",
        ],
        name="date",
    )
    result = helpers.vectorised.is_long_day(dates)
    assert not result.any()


def test_is_short_day_tz_aware_true():
    dates = pd.DatetimeIndex(
        [
            "2019-03-31",
            "2020-03-29",
            "2021-03-28",
            "2022-03-27",
            "2023-03-26",
            "2024-03-31",
        ],
        name="date",
        tz="CET",
    )
    result = helpers.vectorised.is_short_day(dates)
    assert result.all()


def test_is_short_day_tz_aware_false():
    dates = pd.DatetimeIndex(
        [
            "2020-03-31",
            "2021-03-29",
            "2022-03-28",
            "2023-03-27",
            "2024-03-26",
            "2025-03-31",
            "2020-10-25",
            "2021-10-31",
            "2022-10-30",
            "2023-10-29",
            "2024-10-27",
        ],
        name="date",
        tz="CET",
    )
    result = helpers.vectorised.is_short_day(dates)
    assert not result.any()


def test_is_long_day_tz_aware_true():
    dates = pd.DatetimeIndex(
        [
            "2020-10-25",
            "2021-10-31",
            "2022-10-30",
            "2023-10-29",
            "2024-10-27",
        ],
        name="date",
        tz="UTC",
    )
    result = helpers.vectorised.is_long_day(dates)
    assert result.all()


def test_is_long_day_tz_aware_false():
    dates = pd.DatetimeIndex(
        [
            "2021-10-25",
            "2022-10-31",
            "2023-10-30",
            "2024-10-29",
            "2025-10-27",
            "2019-03-31",
            "2020-03-29",
            "2021-03-28",
            "2022-03-27",
            "2023-03-26",
            "2024-03-31",
        ],
        name="date",
        tz="UTC",
    )
    result = helpers.vectorised.is_long_day(dates)
    assert not result.any()


def test_utc_from_sp_winter():
    settlement_date = "2021-03-01"
    settlement_periods = np.arange(1, 49)

    df = pd.DataFrame(
        {"settlement_period": settlement_periods},
    )
    df["settlement_date"] = settlement_date

    expected = pd.DatetimeIndex(
        [
            "2021-03-01 00:00",
            "2021-03-01 00:30",
            "2021-03-01 01:00",
            "2021-03-01 01:30",
            "2021-03-01 02:00",
            "2021-03-01 02:30",
            "2021-03-01 03:00",
            "2021-03-01 03:30",
            "2021-03-01 04:00",
            "2021-03-01 04:30",
            "2021-03-01 05:00",
            "2021-03-01 05:30",
            "2021-03-01 06:00",
            "2021-03-01 06:30",
            "2021-03-01 07:00",
            "2021-03-01 07:30",
            "2021-03-01 08:00",
            "2021-03-01 08:30",
            "2021-03-01 09:00",
            "2021-03-01 09:30",
            "2021-03-01 10:00",
            "2021-03-01 10:30",
            "2021-03-01 11:00",
            "2021-03-01 11:30",
            "2021-03-01 12:00",
            "2021-03-01 12:30",
            "2021-03-01 13:00",
            "2021-03-01 13:30",
            "2021-03-01 14:00",
            "2021-03-01 14:30",
            "2021-03-01 15:00",
            "2021-03-01 15:30",
            "2021-03-01 16:00",
            "2021-03-01 16:30",
            "2021-03-01 17:00",
            "2021-03-01 17:30",
            "2021-03-01 18:00",
            "2021-03-01 18:30",
            "2021-03-01 19:00",
            "2021-03-01 19:30",
            "2021-03-01 20:00",
            "2021-03-01 20:30",
            "2021-03-01 21:00",
            "2021-03-01 21:30",
            "2021-03-01 22:00",
            "2021-03-01 22:30",
            "2021-03-01 23:00",
            "2021-03-01 23:30",
        ],
        tz="UTC",
    ).to_series()
    result = helpers.vectorised.utc_from_sp(
        df["settlement_date"], df["settlement_period"]
    )
    pd.testing.assert_series_equal(result, expected, check_index=False)


def test_utc_from_sp_summer():
    settlement_date = "2021-06-01"
    settlement_periods = np.arange(1, 49)
    df = pd.DataFrame(
        {"settlement_period": settlement_periods},
    )
    df["settlement_date"] = settlement_date
    expected = pd.DatetimeIndex(
        [
            "2021-05-31 23:00",
            "2021-05-31 23:30",
            "2021-06-01 00:00",
            "2021-06-01 00:30",
            "2021-06-01 01:00",
            "2021-06-01 01:30",
            "2021-06-01 02:00",
            "2021-06-01 02:30",
            "2021-06-01 03:00",
            "2021-06-01 03:30",
            "2021-06-01 04:00",
            "2021-06-01 04:30",
            "2021-06-01 05:00",
            "2021-06-01 05:30",
            "2021-06-01 06:00",
            "2021-06-01 06:30",
            "2021-06-01 07:00",
            "2021-06-01 07:30",
            "2021-06-01 08:00",
            "2021-06-01 08:30",
            "2021-06-01 09:00",
            "2021-06-01 09:30",
            "2021-06-01 10:00",
            "2021-06-01 10:30",
            "2021-06-01 11:00",
            "2021-06-01 11:30",
            "2021-06-01 12:00",
            "2021-06-01 12:30",
            "2021-06-01 13:00",
            "2021-06-01 13:30",
            "2021-06-01 14:00",
            "2021-06-01 14:30",
            "2021-06-01 15:00",
            "2021-06-01 15:30",
            "2021-06-01 16:00",
            "2021-06-01 16:30",
            "2021-06-01 17:00",
            "2021-06-01 17:30",
            "2021-06-01 18:00",
            "2021-06-01 18:30",
            "2021-06-01 19:00",
            "2021-06-01 19:30",
            "2021-06-01 20:00",
            "2021-06-01 20:30",
            "2021-06-01 21:00",
            "2021-06-01 21:30",
            "2021-06-01 22:00",
            "2021-06-01 22:30",
        ],
        tz="UTC",
    ).to_series()
    result = helpers.vectorised.utc_from_sp(
        df["settlement_date"], df["settlement_period"]
    )
    pd.testing.assert_series_equal(result, expected, check_index=False)


def test_utc_from_settlement_date_long_day():
    settlement_date = "2020-10-25"
    settlement_periods = np.arange(1, 51)
    df = pd.DataFrame(
        {"settlement_period": settlement_periods},
    )
    df["settlement_date"] = settlement_date
    expected = pd.date_range(
        "2020-10-24 23:00", periods=50, freq="30min", tz="UTC"
    ).to_series()
    result = helpers.vectorised.utc_from_sp(df.settlement_date, df.settlement_period)
    pd.testing.assert_series_equal(result, expected, check_index=False)


def test_utc_from_settlement_date_short_day():
    settlement_date = "2021-03-28"
    settlement_periods = np.arange(1, 47)
    df = pd.DataFrame(
        {"settlement_period": settlement_periods},
    )
    df["settlement_date"] = settlement_date
    expected = pd.date_range(
        "2021-03-28 00:00", periods=46, freq="30min", tz="UTC"
    ).to_series()
    result = helpers.vectorised.utc_from_sp(df.settlement_date, df.settlement_period)
    pd.testing.assert_series_equal(result, expected, check_index=False)


def test_sp_from_timestamps_winter_utc():
    """For a normal (not clock-change) winter day,
    the times are equivalent to Europe/London

    Returned series should have the same index as the series passed to the function
    """
    settlement_date = "2023-03-01"
    timestamps = pd.date_range(
        settlement_date, periods=48, freq="30min", tz="UTC"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = pd.to_datetime(timestamps.dt.date)
    expected_periods = pd.Series(range(1, 49), index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_summer_utc():
    """For a normal (not clock-change) summer day,
    local London times are offset by 1 hour from UTC
    the midnight (Europe/London) SP will be 1
    so the midnight (UTC) SP will be 3

    Returned series should have the same index as the series passed to the function

    See also:

    test_sp_from_timestamps_summer_utc2

    """
    settlement_date = "2023-06-01"
    timestamps = pd.date_range(
        settlement_date, periods=48, freq="30min", tz="UTC"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = [settlement_date] * 46 + ["2023-06-02"] * 2
    expected_dates = pd.to_datetime(expected_dates).to_series(index=timestamps.index)
    expected_period_values = [(i + 2) % 48 + 1 for i in range(48)]
    expected_periods = pd.Series(expected_period_values, index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_summer_utc2():
    """For a normal (not clock-change) summer day,
    local London times are offset by 1 hour from UTC
    the midnight (Europe/London) SP will be 1
    so the midnight (UTC) SP will be 3

    Returned series should have the same index as the series passed to the function

    Notionally simplified version of the above test
    """
    settlement_date = "2023-06-01"
    start_time = pd.Timestamp("2023-05-31 23:00", tz="UTC")

    timestamps = pd.date_range(
        start_time, periods=48, freq="30min", tz="UTC"
    ).to_series()
    expected_index = timestamps.index
    local_timestamps = timestamps.tz_convert("Europe/London")
    expected_dates = pd.Series(
        [pd.Timestamp(settlement_date)] * 48, index=expected_index
    )
    expected_dates = pd.to_datetime(expected_dates)
    expected_periods = pd.Series(range(1, 49), index=expected_index)
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    pd.testing.assert_series_equal(settlement_dates, expected_dates, check_index=False)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_long_day_utc():
    """For a long clock change day,
    times start in the normal summertime mode (starting SP 3
    and run through to 50 (rather than restarting after 48)
    """
    settlement_date = "2020-10-25"
    timestamps = pd.date_range(
        settlement_date, periods=50, freq="30min", tz="UTC"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = pd.to_datetime(timestamps.dt.date)
    # settlement periods start at 3
    expected_period_values = [i % 50 + 1 for i in range(52)]
    expected_periods = pd.Series(expected_period_values[2:], index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_short_day_utc():
    """For a short clock change day,
    times start in the normal wintertime mode (starting SP 1)
    and restart after 46
    """
    settlement_date = "2021-03-28"
    timestamps = pd.date_range(
        settlement_date, periods=46, freq="30min", tz="UTC"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = pd.to_datetime(timestamps.dt.date)
    # settlement periods start at 3
    expected_period_values = [i % 46 + 1 for i in range(46)]
    expected_periods = pd.Series(expected_period_values, index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamp_strings():
    # long/short days don't matter for this function because using utc input
    settlement_date = "2021-03-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "UTC"
    timestamp_strings = pd.Series(
        [
            f"{settlement_date}T00:00+0000",
            f"{settlement_date}T00:30+0000",
            f"{settlement_date}T01:00+0000",
            f"{settlement_date}T01:30+0000",
            f"{settlement_date}T02:00+0000",
            f"{settlement_date}T02:30+0000",
            f"{settlement_date}T03:00+0000",
            f"{settlement_date}T03:30+0000",
            f"{settlement_date}T04:00+0000",
            f"{settlement_date}T04:30+0000",
            f"{settlement_date}T05:00+0000",
            f"{settlement_date}T05:30+0000",
            f"{settlement_date}T06:00+0000",
            f"{settlement_date}T06:30+0000",
            f"{settlement_date}T07:00+0000",
            f"{settlement_date}T07:30+0000",
            f"{settlement_date}T08:00+0000",
            f"{settlement_date}T08:30+0000",
            f"{settlement_date}T09:00+0000",
            f"{settlement_date}T09:30+0000",
            f"{settlement_date}T10:00+0000",
            f"{settlement_date}T10:30+0000",
            f"{settlement_date}T11:00+0000",
            f"{settlement_date}T11:30+0000",
            f"{settlement_date}T12:00+0000",
            f"{settlement_date}T12:30+0000",
            f"{settlement_date}T13:00+0000",
            f"{settlement_date}T13:30+0000",
            f"{settlement_date}T14:00+0000",
            f"{settlement_date}T14:30+0000",
            f"{settlement_date}T15:00+0000",
            f"{settlement_date}T15:30+0000",
            f"{settlement_date}T16:00+0000",
            f"{settlement_date}T16:30+0000",
            f"{settlement_date}T17:00+0000",
            f"{settlement_date}T17:30+0000",
            f"{settlement_date}T18:00+0000",
            f"{settlement_date}T18:30+0000",
            f"{settlement_date}T19:00+0000",
            f"{settlement_date}T19:30+0000",
            f"{settlement_date}T20:00+0000",
            f"{settlement_date}T20:30+0000",
            f"{settlement_date}T21:00+0000",
            f"{settlement_date}T21:30+0000",
            f"{settlement_date}T22:00+0000",
            f"{settlement_date}T22:30+0000",
            f"{settlement_date}T23:00+0000",
            f"{settlement_date}T23:30+0000",
        ]
    )
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamp_strings
    )
    expected_dates = pd.to_datetime(pd.Series([settlement_date_obj] * 48))
    expected_periods = pd.Series(range(1, 49))
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


@pytest.mark.parametrize(
    "settlement_date", ["2021-03-01", "2021-06-01", "2020-10-25", "2021-03-28"]
)
def test_sp_from_timestamps_winter_tz_naive(settlement_date):
    """For a naive timestamp, assume London local timezone"""
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    naive = pd.Timestamp(f"{settlement_date} 00:00")

    naive = pd.Series(
        [
            pd.Timestamp(f"{settlement_date} 00:00"),
            pd.Timestamp(f"{settlement_date} 00:30"),
            pd.Timestamp(f"{settlement_date} 23:00"),
            pd.Timestamp(f"{settlement_date} 23:30"),
        ]
    )
    london = naive.dt.tz_localize("Europe/London")

    sd, sp = helpers.vectorised.sp_from_timestamps(naive)

    naive_dates, naive_periods = helpers.vectorised.sp_from_timestamps(naive)
    london_dates, london_periods = helpers.vectorised.sp_from_timestamps(london)

    assert naive_dates.equals(london_dates)
    assert naive_periods.equals(london_periods)


@pytest.mark.parametrize("settlement_date", ["2021-03-28"])
def test_sp_from_timestamps_spring_clock_change_naive_raises_exception(settlement_date):
    """For a naive timestamp, assume London local timezone.

    But if you try to pass a timestamp that is ambiguous, it will raise an error"""
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    naive = pd.Timestamp(f"{settlement_date} 00:00")

    naive = pd.Series(
        [
            pd.Timestamp(f"{settlement_date} 00:00"),
            pd.Timestamp(f"{settlement_date} 00:30"),
            # 01:00 would raise an error here
            pd.Timestamp(f"{settlement_date} 01:00"),
            pd.Timestamp(f"{settlement_date} 23:00"),
            pd.Timestamp(f"{settlement_date} 23:30"),
        ]
    )

    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        sd, sp = helpers.vectorised.sp_from_timestamps(naive)


def test_sp_from_timestamp_summer_london():
    """If the timestamp is given in London time,
    always expect settlement period to follow same convention.

    For non-clock-change days, SP1 starts at midnight, SP48 starts at 23:30

    For clock-change days, there with either be two hours from 1-2 (long day)
    or no hours from 1-2 (short day).

    This will throw and error, and is a good reason to avoid this timezone.

    However the timezone allows for 'intuitive' tests, given that the
    settlement periods are based around this time zone
    """

    settlement_date = "2023-06-01"
    tz = "Europe/London"
    start_time = pd.Timestamp("2023-06-01 00:00", tz=tz)

    timestamps = pd.date_range(start_time, periods=48, freq="30min", tz=tz).to_series()
    expected_index = timestamps.index
    local_timestamps = timestamps.tz_convert("Europe/London")
    expected_dates = pd.Series(
        [pd.Timestamp(settlement_date)] * 48, index=expected_index
    )
    expected_dates = pd.to_datetime(expected_dates)
    expected_periods = pd.Series(range(1, 49), index=expected_index)
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    pd.testing.assert_series_equal(settlement_dates, expected_dates, check_index=False)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_long_day_london():
    """If the timestamp is given in London time,
    always expect settlement period to follow same convention.

    For non-clock-change days, SP1 starts at midnight, SP48 starts at 23:30

    For clock-change days, there with either be two hours from 1-2 (long day)
    or no hours from 1-2 (short day).

    This will throw and error, and is a good reason to avoid this timezone.

    However the timezone allows for 'intuitive' tests, given that the
    settlement periods are based around this time zone
    """
    settlement_date = "2020-10-25"
    timestamps = pd.date_range(
        settlement_date, periods=50, freq="30min", tz="Europe/London"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = pd.to_datetime(timestamps.dt.date)
    expected_periods = pd.Series(range(1, 51), index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)


def test_sp_from_timestamps_short_day_london():
    """If the timestamp is given in London time,
    always expect settlement period to follow same convention.

    For non-clock-change days, SP1 starts at midnight, SP48 starts at 23:30

    For clock-change days, there with either be two hours from 1-2 (long day)
    or no hours from 1-2 (short day).

    This will throw and error, and is a good reason to avoid this timezone.

    However the timezone allows for 'intuitive' tests, given that the
    settlement periods are based around this time zone
    """
    settlement_date = "2021-03-28"
    timestamps = pd.date_range(
        settlement_date, periods=46, freq="30min", tz="Europe/London"
    ).to_series()
    settlement_dates, settlement_periods = helpers.vectorised.sp_from_timestamps(
        timestamps
    )
    expected_dates = pd.to_datetime(timestamps.dt.date)
    # settlement periods start at 3
    expected_period_values = [i % 46 + 1 for i in range(46)]
    expected_periods = pd.Series(expected_period_values, index=timestamps.index)
    pd.testing.assert_series_equal(settlement_dates, expected_dates)
    pd.testing.assert_series_equal(settlement_periods, expected_periods)
