import datetime as dt
import pytest
from efa.efaday import EFADay

def test_init_date_string():
    # Create an EFADay object with a date string
    efa_day = EFADay("2022-01-01")

    assert efa_day.date == dt.date(2022, 1, 1)

def test_init_date_object():
    # Create an EFADay object with a date object
    efa_day = EFADay(dt.date(2022, 1, 1))

    assert efa_day.date == dt.date(2022, 1, 1)

def test_start_time_winter_day():
    # Create an EFADay object for a winter day
    efa_day = EFADay("2022-01-01")

    assert efa_day.start_time == dt.datetime(2021, 12, 31, 23, 0, 0, tzinfo=dt.timezone.utc)

def test_start_time_summer_day():
    # Create an EFADay object for a summer day
    efa_day = EFADay("2022-07-01")

    assert efa_day.start_time == dt.datetime(2022, 6, 30, 22, 0, 0, tzinfo=dt.timezone.utc)

def test_start_time_winter_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-10-30")

    assert efa_day.start_time == dt.datetime(2022, 10, 29, 22, 0, 0, tzinfo=dt.timezone.utc)

def test_start_time_summer_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-03-27")

    assert efa_day.start_time == dt.datetime(2022, 3, 26, 23, 0, 0, tzinfo=dt.timezone.utc)


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

    assert efa_day.end_time == dt.datetime(2022, 10, 30, 23, 0, 0, tzinfo=dt.timezone.utc)

def test_end_time_summer_clock_change_day():
    # Create an EFADay object for a day when the clock changes
    efa_day = EFADay("2022-03-27")

    assert efa_day.end_time == dt.datetime(2022, 3, 27, 22, 0, 0, tzinfo=dt.timezone.utc)


