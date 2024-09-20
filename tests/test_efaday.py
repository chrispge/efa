import datetime as dt

import pandas as pd
import pytest

from efa.efaday import EFADay


def test_import_efaday():
    # Check that the EFADay class can be imported
    from efa import EFADay


def test_init_date_string():
    # Create an EFADay object with a date string
    efa_day = EFADay("2022-01-01")

    assert efa_day.date == dt.date(2022, 1, 1)


def test_init_date_object():
    # Create an EFADay object with a date object
    efa_day = EFADay(dt.date(2022, 1, 1))

    assert efa_day.date == dt.date(2022, 1, 1)


def test_init_efa_day():
    # Create an EFADay object with another EFADay object
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay(efa_day1)

    assert efa_day1 == efa_day2


def test__str__():
    # Create an EFADay object
    efa_day = EFADay("2022-01-01")

    assert str(efa_day) == "2022-01-01"


def test__repr__():
    # Create an EFADay object
    efa_day = EFADay("2022-01-01")

    assert repr(efa_day) == "EFADay('2022-01-01')"
    assert eval(repr(efa_day)) == efa_day


def test__eq__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert efa_day1 == efa_day2


def test_not__eq__():
    # Compare an EFADay object with a date object
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = dt.date(2022, 1, 1)

    assert not efa_day1 == efa_day2


def test__ne__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert efa_day1 != efa_day2


def test_not__ne__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert not efa_day1 != efa_day2


def test__lt__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert efa_day1 < efa_day2


def test_not__lt__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert not efa_day1 < efa_day2


def test__le__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert efa_day1 <= efa_day2


def test_not__le__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert not efa_day2 <= efa_day1


def test__gt__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert efa_day2 > efa_day1


def test_not__gt__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert not efa_day1 > efa_day2


def test__ge__():
    # Create two EFADay objects with the same date
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert efa_day1 >= efa_day2


def test_not__ge__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert not efa_day1 >= efa_day2


def test__hash__():
    # Create an EFADay object
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-01")

    assert hash(efa_day1) == hash(efa_day2)


def test_not__hash__():
    # Create two EFADay objects with different dates
    efa_day1 = EFADay("2022-01-01")
    efa_day2 = EFADay("2022-01-02")

    assert hash(efa_day1) != hash(efa_day2)


def test_start_time_winter_day():
    # Create an EFADay object for a winter day
    efa_day = EFADay("2022-01-01")

    assert efa_day.start_time == dt.datetime(
        2021, 12, 31, 23, 0, 0, tzinfo=dt.timezone.utc
    )


def test_start_time_summer_day():
    # Create an EFADay object for a summer day
    efa_day = EFADay("2022-07-01")

    assert efa_day.start_time == dt.datetime(
        2022, 6, 30, 22, 0, 0, tzinfo=dt.timezone.utc
    )


def test_start_time_winter_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-10-30")

    assert efa_day.start_time == dt.datetime(
        2022, 10, 29, 22, 0, 0, tzinfo=dt.timezone.utc
    )


def test_start_time_summer_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-03-27")

    assert efa_day.start_time == dt.datetime(
        2022, 3, 26, 23, 0, 0, tzinfo=dt.timezone.utc
    )


def test_end_time_winter_day():
    # Create an EFADay object for a winter day
    efa_day = EFADay("2022-01-01")

    assert efa_day.end_time == dt.datetime(2022, 1, 1, 23, 0, 0, tzinfo=dt.timezone.utc)


def test_end_time_summer_day():
    # Create an EFADay object for a summer day
    efa_day = EFADay("2022-07-01")

    assert efa_day.end_time == dt.datetime(2022, 7, 1, 22, 0, 0, tzinfo=dt.timezone.utc)


def test_end_time_winter_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-10-30")

    assert efa_day.end_time == dt.datetime(
        2022, 10, 30, 23, 0, 0, tzinfo=dt.timezone.utc
    )


def test_end_time_summer_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-03-27")

    assert efa_day.end_time == dt.datetime(
        2022, 3, 27, 22, 0, 0, tzinfo=dt.timezone.utc
    )


# last SP start time


def test_last_sp_start_time_winter_day():
    # Create an EFADay object for a winter day
    efa_day = EFADay("2022-01-01")

    assert efa_day.last_sp_start_time == dt.datetime(
        2022, 1, 1, 22, 30, 0, tzinfo=dt.timezone.utc
    )


def test_last_sp_start_time_summer_day():
    # Create an EFADay object for a summer day
    efa_day = EFADay("2022-07-01")

    assert efa_day.last_sp_start_time == dt.datetime(
        2022, 7, 1, 21, 30, 0, tzinfo=dt.timezone.utc
    )


def test_last_sp_start_time_winter_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-10-30")

    assert efa_day.last_sp_start_time == dt.datetime(
        2022, 10, 30, 22, 30, 0, tzinfo=dt.timezone.utc
    )


def test_last_sp_start_time_summer_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-03-27")

    assert efa_day.last_sp_start_time == dt.datetime(
        2022, 3, 27, 21, 30, 0, tzinfo=dt.timezone.utc
    )


# gas day
def test_gas_day_winter():
    # Create an EFADay object for a gas day
    efa_day = EFADay("2022-01-01")

    assert efa_day.gas_day == dt.datetime(2022, 1, 1, 6, 0, 0, tzinfo=dt.timezone.utc)


def test_gas_day_summer():
    # Create an EFADay object for a gas day
    efa_day = EFADay("2022-06-01")

    assert efa_day.gas_day == dt.datetime(2022, 6, 1, 5, 0, 0, tzinfo=dt.timezone.utc)


def test_end_time_winter_clock_change_day():
    efa_day = EFADay("2022-10-30")

    assert efa_day.gas_day == dt.datetime(2022, 10, 30, 6, 0, 0, tzinfo=dt.timezone.utc)


def test_end_time_summer_clock_change_day():
    efa_day = EFADay("2022-03-27")

    assert efa_day.gas_day == dt.datetime(2022, 3, 27, 5, 0, 0, tzinfo=dt.timezone.utc)


def test__add__():
    efa_date = EFADay("2022-01-01")
    result = efa_date + 1
    assert result == EFADay("2022-01-02")


def test__sub__():
    efa_date = EFADay("2022-01-01")
    result = efa_date - 1
    assert result == EFADay("2021-12-31")


def test__add__non_int():
    efa_date = EFADay("2022-01-01")
    with pytest.raises(TypeError):
        efa_date + 3.14


def test_from_start_time_winter():
    start_time = dt.datetime(2022, 1, 1, 0, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-01-01")

    start_time = dt.datetime(2022, 1, 1, 1, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-01-01")

    start_time = dt.datetime(2022, 1, 1, 16, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-01-01")

    start_time = dt.datetime(2022, 1, 1, 23, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-01-02")

    start_time = dt.datetime(2022, 1, 1, 23, 30, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-01-02")


def test_from_start_time_summer():
    start_time = dt.datetime(2022, 6, 1, 0, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-06-01")

    start_time = dt.datetime(2022, 6, 1, 1, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-06-01")

    start_time = dt.datetime(2022, 6, 1, 21, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-06-01")

    start_time = dt.datetime(2022, 6, 1, 22, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-06-02")

    start_time = dt.datetime(2022, 6, 1, 23, 0, 0, tzinfo=dt.timezone.utc)
    result = EFADay.from_start_time(start_time)
    assert result == EFADay("2022-06-02")


def test_hourly_index_winter():
    efa_date = EFADay("2022-01-01")
    result = efa_date.start_time_index("60min")
    assert result[0] == pd.Timestamp("2021-12-31 23:00:00", tz="UTC")
    assert result[-1] == pd.Timestamp("2022-01-01 22:00:00", tz="UTC")
    assert len(result) == 24
    assert result.is_monotonic_increasing


def test_hourly_index_summer():
    efa_date = EFADay("2022-06-01")
    result = efa_date.start_time_index("60min")
    assert result[0] == pd.Timestamp("2022-05-31 22:00:00", tz="UTC")
    assert result[-1] == pd.Timestamp("2022-06-01 21:00:00", tz="UTC")
    assert len(result) == 24
    assert result.is_monotonic_increasing


def test_hourly_index_spring_clock_change():
    efa_date = EFADay("2022-03-27")
    result = efa_date.start_time_index("60min")
    assert result[0] == pd.Timestamp("2022-03-26 23:00:00", tz="UTC")
    assert result[-1] == pd.Timestamp("2022-03-27 21:00:00", tz="UTC")
    assert len(result) == 23
    assert result.is_monotonic_increasing


def test_hourly_index_autumn_clock_change():
    efa_date = EFADay("2022-10-30")
    result = efa_date.start_time_index("60min")
    assert result[0] == pd.Timestamp("2022-10-29 22:00:00", tz="UTC")
    assert result[-1] == pd.Timestamp("2022-10-30 22:00:00", tz="UTC")
    assert len(result) == 25
    assert result.is_monotonic_increasing


def test_half_hourly_index_winter():
    efa_date = EFADay("2022-01-01")
    result = efa_date.start_time_index("30min")
    assert result[0] == pd.Timestamp("2021-12-31 23:00:00", tz="UTC")
    assert result[-1] == pd.Timestamp("2022-01-01 22:30:00", tz="UTC")
    assert len(result) == 48
    assert result.is_monotonic_increasing
