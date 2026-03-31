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


def test_hourly_index_summer():
    efa_date = EFADay("2022-06-01")
    result = efa_date.start_time_index("60min", tz="Europe/London")
    assert result[0] == pd.Timestamp("2022-05-31 23:00:00", tz="Europe/London")
    assert result[-1] == pd.Timestamp("2022-06-01 22:00:00", tz="Europe/London")
    assert len(result) == 24
    assert result.is_monotonic_increasing


def test_current_date():
    efa_date = EFADay()
    today = pd.Timestamp.utcnow().tz_convert("Europe/Paris").date()
    assert efa_date.date == today


def test_start_time_from_utc_str():
    efa_date = EFADay("2022-01-01")
    utc_str = "2300"
    result = efa_date.start_time_from_utc_str(utc_str)
    print(result)
    assert result == pd.Timestamp("2021-12-31 23:00:00+00")
    utc_str = "0000"
    result = efa_date.start_time_from_utc_str(utc_str)
    print(result)
    assert result == pd.Timestamp("2022-01-01 00:00:00+00")


def test_start_time_from_utc_str_summer():
    efa_date = EFADay("2022-06-01")
    utc_str = "2200"
    result = efa_date.start_time_from_utc_str(utc_str)
    print(result)
    assert result == pd.Timestamp("2022-05-31 22:00:00+00")
    utc_str = "2300"
    result = efa_date.start_time_from_utc_str(utc_str)
    assert result == pd.Timestamp("2022-05-31 23:00:00+00")
    utc_str = "0000"
    result = efa_date.start_time_from_utc_str(utc_str)
    assert result == pd.Timestamp("2022-06-01 00:00:00+00")


def test_efa_sp_from_utc():
    """Test EFA SP (not real SP) calculation"""
    efa_date = EFADay("2026-01-01")
    start_time = pd.Timestamp("2025-12-31 23:00:00+00")
    assert efa_date.efa_sp_from_utc(start_time) == 1
    start_time = pd.Timestamp("2026-01-01 22:30:00+00")
    assert efa_date.efa_sp_from_utc(start_time) == 48

    long_date = EFADay("2025-10-26")
    start_time = pd.Timestamp("2025-10-25 22:00:00+00")
    assert long_date.efa_sp_from_utc(start_time) == 1
    start_time = pd.Timestamp("2025-10-26 22:30:00+00")
    assert long_date.efa_sp_from_utc(start_time) == 50


def test_efa_sp_from_utc_bad_time():
    efa_date = EFADay("2026-01-01")
    start_time = pd.Timestamp("2025-12-31 22:59:00+00")
    with pytest.raises(ValueError):
        efa_date.efa_sp_from_utc(start_time)
    start_time = pd.Timestamp("2025-01-01 23:01:00+00")
    with pytest.raises(ValueError):
        efa_date.efa_sp_from_utc(start_time)


def test_efa_sp_from_utc_non_hh_time():
    efa_date = EFADay("2026-01-01")
    start_time = pd.Timestamp("2026-01-01 00:17:00+00")
    assert efa_date.efa_sp_from_utc(start_time) == 3


def test_efa_sp_from_utc_bad_time():
    efa_date = EFADay("2026-01-01")
    start_time = pd.Timestamp("2024-12-31 23:00:00+00")
    with pytest.raises(ValueError):
        efa_date.efa_sp_from_utc(start_time)


def test_utc_from_efa_sp():
    efa_date = EFADay("2026-01-01")
    assert efa_date.utc_from_efa_sp(1) == pd.Timestamp("2025-12-31 23:00:00+00")
    assert efa_date.utc_from_efa_sp(48) == pd.Timestamp("2026-01-01 22:30:00+00")
    long_date = EFADay("2025-10-26")
    assert long_date.utc_from_efa_sp(1) == pd.Timestamp("2025-10-25 22:00:00+00")
    assert long_date.utc_from_efa_sp(50) == pd.Timestamp("2025-10-26 22:30:00+00")


def test_utc_from_efa_sp_bad_sp():
    efa_date = EFADay("2026-01-01")
    with pytest.raises(ValueError):
        efa_date.utc_from_efa_sp(0)
    with pytest.raises(ValueError):
        efa_date.utc_from_efa_sp(49)
    with pytest.raises(ValueError):
        efa_date.utc_from_efa_sp(1.5)


def test_make_hh_options_winter_day():
    efa_date = EFADay("2026-01-01")
    result = efa_date.make_hh_options()
    print(result)
    expected = [
        {"label": "23:00", "value": "01"},
        {"label": "23:30", "value": "02"},
        {"label": "00:00", "value": "03"},
        {"label": "00:30", "value": "04"},
        {"label": "01:00", "value": "05"},
        {"label": "01:30", "value": "06"},
        {"label": "02:00", "value": "07"},
        {"label": "02:30", "value": "08"},
        {"label": "03:00", "value": "09"},
        {"label": "03:30", "value": "10"},
        {"label": "04:00", "value": "11"},
        {"label": "04:30", "value": "12"},
        {"label": "05:00", "value": "13"},
        {"label": "05:30", "value": "14"},
        {"label": "06:00", "value": "15"},
        {"label": "06:30", "value": "16"},
        {"label": "07:00", "value": "17"},
        {"label": "07:30", "value": "18"},
        {"label": "08:00", "value": "19"},
        {"label": "08:30", "value": "20"},
        {"label": "09:00", "value": "21"},
        {"label": "09:30", "value": "22"},
        {"label": "10:00", "value": "23"},
        {"label": "10:30", "value": "24"},
        {"label": "11:00", "value": "25"},
        {"label": "11:30", "value": "26"},
        {"label": "12:00", "value": "27"},
        {"label": "12:30", "value": "28"},
        {"label": "13:00", "value": "29"},
        {"label": "13:30", "value": "30"},
        {"label": "14:00", "value": "31"},
        {"label": "14:30", "value": "32"},
        {"label": "15:00", "value": "33"},
        {"label": "15:30", "value": "34"},
        {"label": "16:00", "value": "35"},
        {"label": "16:30", "value": "36"},
        {"label": "17:00", "value": "37"},
        {"label": "17:30", "value": "38"},
        {"label": "18:00", "value": "39"},
        {"label": "18:30", "value": "40"},
        {"label": "19:00", "value": "41"},
        {"label": "19:30", "value": "42"},
        {"label": "20:00", "value": "43"},
        {"label": "20:30", "value": "44"},
        {"label": "21:00", "value": "45"},
        {"label": "21:30", "value": "46"},
        {"label": "22:00", "value": "47"},
        {"label": "22:30", "value": "48"},
    ]
    assert result == expected


def test_make_hh_options_summer_day():
    efa_date = EFADay("2026-06-01")
    result = efa_date.make_hh_options()
    print(result)
    expected = [
        {"label": "23:00", "value": "01"},
        {"label": "23:30", "value": "02"},
        {"label": "00:00", "value": "03"},
        {"label": "00:30", "value": "04"},
        {"label": "01:00", "value": "05"},
        {"label": "01:30", "value": "06"},
        {"label": "02:00", "value": "07"},
        {"label": "02:30", "value": "08"},
        {"label": "03:00", "value": "09"},
        {"label": "03:30", "value": "10"},
        {"label": "04:00", "value": "11"},
        {"label": "04:30", "value": "12"},
        {"label": "05:00", "value": "13"},
        {"label": "05:30", "value": "14"},
        {"label": "06:00", "value": "15"},
        {"label": "06:30", "value": "16"},
        {"label": "07:00", "value": "17"},
        {"label": "07:30", "value": "18"},
        {"label": "08:00", "value": "19"},
        {"label": "08:30", "value": "20"},
        {"label": "09:00", "value": "21"},
        {"label": "09:30", "value": "22"},
        {"label": "10:00", "value": "23"},
        {"label": "10:30", "value": "24"},
        {"label": "11:00", "value": "25"},
        {"label": "11:30", "value": "26"},
        {"label": "12:00", "value": "27"},
        {"label": "12:30", "value": "28"},
        {"label": "13:00", "value": "29"},
        {"label": "13:30", "value": "30"},
        {"label": "14:00", "value": "31"},
        {"label": "14:30", "value": "32"},
        {"label": "15:00", "value": "33"},
        {"label": "15:30", "value": "34"},
        {"label": "16:00", "value": "35"},
        {"label": "16:30", "value": "36"},
        {"label": "17:00", "value": "37"},
        {"label": "17:30", "value": "38"},
        {"label": "18:00", "value": "39"},
        {"label": "18:30", "value": "40"},
        {"label": "19:00", "value": "41"},
        {"label": "19:30", "value": "42"},
        {"label": "20:00", "value": "43"},
        {"label": "20:30", "value": "44"},
        {"label": "21:00", "value": "45"},
        {"label": "21:30", "value": "46"},
        {"label": "22:00", "value": "47"},
        {"label": "22:30", "value": "48"},
    ]
    assert result == expected


def test_make_hh_options_short_day():
    efa_date = EFADay("2026-03-29")
    result = efa_date.make_hh_options()
    expected = [
        {"label": "23:00", "value": "01"},
        {"label": "23:30", "value": "02"},
        {"label": "00:00", "value": "03"},
        {"label": "00:30", "value": "04"},
        {"label": "02:00", "value": "05"},
        {"label": "02:30", "value": "06"},
        {"label": "03:00", "value": "07"},
        {"label": "03:30", "value": "08"},
        {"label": "04:00", "value": "09"},
        {"label": "04:30", "value": "10"},
        {"label": "05:00", "value": "11"},
        {"label": "05:30", "value": "12"},
        {"label": "06:00", "value": "13"},
        {"label": "06:30", "value": "14"},
        {"label": "07:00", "value": "15"},
        {"label": "07:30", "value": "16"},
        {"label": "08:00", "value": "17"},
        {"label": "08:30", "value": "18"},
        {"label": "09:00", "value": "19"},
        {"label": "09:30", "value": "20"},
        {"label": "10:00", "value": "21"},
        {"label": "10:30", "value": "22"},
        {"label": "11:00", "value": "23"},
        {"label": "11:30", "value": "24"},
        {"label": "12:00", "value": "25"},
        {"label": "12:30", "value": "26"},
        {"label": "13:00", "value": "27"},
        {"label": "13:30", "value": "28"},
        {"label": "14:00", "value": "29"},
        {"label": "14:30", "value": "30"},
        {"label": "15:00", "value": "31"},
        {"label": "15:30", "value": "32"},
        {"label": "16:00", "value": "33"},
        {"label": "16:30", "value": "34"},
        {"label": "17:00", "value": "35"},
        {"label": "17:30", "value": "36"},
        {"label": "18:00", "value": "37"},
        {"label": "18:30", "value": "38"},
        {"label": "19:00", "value": "39"},
        {"label": "19:30", "value": "40"},
        {"label": "20:00", "value": "41"},
        {"label": "20:30", "value": "42"},
        {"label": "21:00", "value": "43"},
        {"label": "21:30", "value": "44"},
        {"label": "22:00", "value": "45"},
        {"label": "22:30", "value": "46"},
    ]
    assert result == expected


def test_make_hh_options_long_day():
    efa_date = EFADay("2026-10-25")
    result = efa_date.make_hh_options()
    print(result)
    expected = [
        {"label": "23:00", "value": "01"},
        {"label": "23:30", "value": "02"},
        {"label": "00:00", "value": "03"},
        {"label": "00:30", "value": "04"},
        {"label": "01:00 (BST)", "value": "05"},
        {"label": "01:30 (BST)", "value": "06"},
        {"label": "01:00 (GMT)", "value": "07"},
        {"label": "01:30 (GMT)", "value": "08"},
        {"label": "02:00", "value": "09"},
        {"label": "02:30", "value": "10"},
        {"label": "03:00", "value": "11"},
        {"label": "03:30", "value": "12"},
        {"label": "04:00", "value": "13"},
        {"label": "04:30", "value": "14"},
        {"label": "05:00", "value": "15"},
        {"label": "05:30", "value": "16"},
        {"label": "06:00", "value": "17"},
        {"label": "06:30", "value": "18"},
        {"label": "07:00", "value": "19"},
        {"label": "07:30", "value": "20"},
        {"label": "08:00", "value": "21"},
        {"label": "08:30", "value": "22"},
        {"label": "09:00", "value": "23"},
        {"label": "09:30", "value": "24"},
        {"label": "10:00", "value": "25"},
        {"label": "10:30", "value": "26"},
        {"label": "11:00", "value": "27"},
        {"label": "11:30", "value": "28"},
        {"label": "12:00", "value": "29"},
        {"label": "12:30", "value": "30"},
        {"label": "13:00", "value": "31"},
        {"label": "13:30", "value": "32"},
        {"label": "14:00", "value": "33"},
        {"label": "14:30", "value": "34"},
        {"label": "15:00", "value": "35"},
        {"label": "15:30", "value": "36"},
        {"label": "16:00", "value": "37"},
        {"label": "16:30", "value": "38"},
        {"label": "17:00", "value": "39"},
        {"label": "17:30", "value": "40"},
        {"label": "18:00", "value": "41"},
        {"label": "18:30", "value": "42"},
        {"label": "19:00", "value": "43"},
        {"label": "19:30", "value": "44"},
        {"label": "20:00", "value": "45"},
        {"label": "20:30", "value": "46"},
        {"label": "21:00", "value": "47"},
        {"label": "21:30", "value": "48"},
        {"label": "22:00", "value": "49"},
        {"label": "22:30", "value": "50"},
    ]
