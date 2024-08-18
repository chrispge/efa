import pandas as pd
import pytest
import pytz

from efa import helpers


@pytest.mark.parametrize(
    "date",
    [
        "2019-03-31",
        "2020-03-29",
        "2021-03-28",
        "2022-03-27",
        "2023-03-26",
        "2024-03-31",
    ],
)
def test_is_short_day_true(date):
    assert helpers.is_short_day(date)


@pytest.mark.parametrize(
    "date",
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
)
def test_is_short_day_false(date):
    assert not helpers.is_short_day(date)


@pytest.mark.parametrize(
    "date",
    [
        "2020-10-25",
        "2021-10-31",
        "2022-10-30",
        "2023-10-29",
        "2024-10-27",
    ],
)
def test_is_long_day_true(date):
    assert helpers.is_long_day(date)


@pytest.mark.parametrize(
    "date",
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
)
def test_is_long_day_false(date):
    assert not helpers.is_long_day(date)


def test_is_long_day_tz_aware_true():
    date = "2020-10-25"
    tz_aware = pd.Timestamp(date).tz_localize("CET")
    assert helpers.is_long_day(tz_aware)


def test_is_long_day_tz_aware_false():
    date = "2020-10-24"
    tz_aware = pd.Timestamp(date).tz_localize("CET")
    assert not helpers.is_long_day(tz_aware)


def test_is_short_day_tz_aware_true():
    date = "2020-03-29"
    tz_aware = pd.Timestamp(date).tz_localize("CET")
    assert helpers.is_short_day(tz_aware)


def test_is_short_day_tz_aware_false():
    date = "2020-03-30"
    tz_aware = pd.Timestamp(date).tz_localize("CET")
    assert not helpers.is_short_day(tz_aware)


def test_utc_from_sp_winter():
    settlement_date = "2021-03-01"
    assert helpers.utc_from_sp(settlement_date, 1) == pd.Timestamp(
        "2021-03-01 00:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 2) == pd.Timestamp(
        "2021-03-01 00:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 3) == pd.Timestamp(
        "2021-03-01 01:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 4) == pd.Timestamp(
        "2021-03-01 01:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 5) == pd.Timestamp(
        "2021-03-01 02:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 6) == pd.Timestamp(
        "2021-03-01 02:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 7) == pd.Timestamp(
        "2021-03-01 03:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 8) == pd.Timestamp(
        "2021-03-01 03:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 9) == pd.Timestamp(
        "2021-03-01 04:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 10) == pd.Timestamp(
        "2021-03-01 04:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 11) == pd.Timestamp(
        "2021-03-01 05:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 12) == pd.Timestamp(
        "2021-03-01 05:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 13) == pd.Timestamp(
        "2021-03-01 06:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 14) == pd.Timestamp(
        "2021-03-01 06:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 15) == pd.Timestamp(
        "2021-03-01 07:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 16) == pd.Timestamp(
        "2021-03-01 07:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 17) == pd.Timestamp(
        "2021-03-01 08:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 18) == pd.Timestamp(
        "2021-03-01 08:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 19) == pd.Timestamp(
        "2021-03-01 09:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 20) == pd.Timestamp(
        "2021-03-01 09:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 21) == pd.Timestamp(
        "2021-03-01 10:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 22) == pd.Timestamp(
        "2021-03-01 10:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 23) == pd.Timestamp(
        "2021-03-01 11:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 24) == pd.Timestamp(
        "2021-03-01 11:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 25) == pd.Timestamp(
        "2021-03-01 12:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 26) == pd.Timestamp(
        "2021-03-01 12:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 27) == pd.Timestamp(
        "2021-03-01 13:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 28) == pd.Timestamp(
        "2021-03-01 13:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 29) == pd.Timestamp(
        "2021-03-01 14:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 30) == pd.Timestamp(
        "2021-03-01 14:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 31) == pd.Timestamp(
        "2021-03-01 15:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 32) == pd.Timestamp(
        "2021-03-01 15:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 33) == pd.Timestamp(
        "2021-03-01 16:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 34) == pd.Timestamp(
        "2021-03-01 16:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 35) == pd.Timestamp(
        "2021-03-01 17:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 36) == pd.Timestamp(
        "2021-03-01 17:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 37) == pd.Timestamp(
        "2021-03-01 18:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 38) == pd.Timestamp(
        "2021-03-01 18:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 39) == pd.Timestamp(
        "2021-03-01 19:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 40) == pd.Timestamp(
        "2021-03-01 19:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 41) == pd.Timestamp(
        "2021-03-01 20:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 42) == pd.Timestamp(
        "2021-03-01 20:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 43) == pd.Timestamp(
        "2021-03-01 21:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 44) == pd.Timestamp(
        "2021-03-01 21:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 45) == pd.Timestamp(
        "2021-03-01 22:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 46) == pd.Timestamp(
        "2021-03-01 22:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 47) == pd.Timestamp(
        "2021-03-01 23:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 48) == pd.Timestamp(
        "2021-03-01 23:30"
    ).tz_localize("UTC")


def test_utc_from_sp_summer():
    settlement_date = "2021-06-01"
    assert helpers.utc_from_sp(settlement_date, 1) == pd.Timestamp(
        "2021-05-31 23:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 2) == pd.Timestamp(
        "2021-05-31 23:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 3) == pd.Timestamp(
        "2021-06-01 00:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 4) == pd.Timestamp(
        "2021-06-01 00:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 5) == pd.Timestamp(
        "2021-06-01 01:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 6) == pd.Timestamp(
        "2021-06-01 01:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 7) == pd.Timestamp(
        "2021-06-01 02:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 8) == pd.Timestamp(
        "2021-06-01 02:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 9) == pd.Timestamp(
        "2021-06-01 03:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 10) == pd.Timestamp(
        "2021-06-01 03:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 11) == pd.Timestamp(
        "2021-06-01 04:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 12) == pd.Timestamp(
        "2021-06-01 04:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 13) == pd.Timestamp(
        "2021-06-01 05:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 14) == pd.Timestamp(
        "2021-06-01 05:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 15) == pd.Timestamp(
        "2021-06-01 06:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 16) == pd.Timestamp(
        "2021-06-01 06:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 17) == pd.Timestamp(
        "2021-06-01 07:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 18) == pd.Timestamp(
        "2021-06-01 07:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 19) == pd.Timestamp(
        "2021-06-01 08:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 20) == pd.Timestamp(
        "2021-06-01 08:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 21) == pd.Timestamp(
        "2021-06-01 09:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 22) == pd.Timestamp(
        "2021-06-01 09:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 23) == pd.Timestamp(
        "2021-06-01 10:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 24) == pd.Timestamp(
        "2021-06-01 10:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 25) == pd.Timestamp(
        "2021-06-01 11:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 26) == pd.Timestamp(
        "2021-06-01 11:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 27) == pd.Timestamp(
        "2021-06-01 12:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 28) == pd.Timestamp(
        "2021-06-01 12:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 29) == pd.Timestamp(
        "2021-06-01 13:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 30) == pd.Timestamp(
        "2021-06-01 13:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 31) == pd.Timestamp(
        "2021-06-01 14:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 32) == pd.Timestamp(
        "2021-06-01 14:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 33) == pd.Timestamp(
        "2021-06-01 15:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 34) == pd.Timestamp(
        "2021-06-01 15:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 35) == pd.Timestamp(
        "2021-06-01 16:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 36) == pd.Timestamp(
        "2021-06-01 16:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 37) == pd.Timestamp(
        "2021-06-01 17:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 38) == pd.Timestamp(
        "2021-06-01 17:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 39) == pd.Timestamp(
        "2021-06-01 18:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 40) == pd.Timestamp(
        "2021-06-01 18:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 41) == pd.Timestamp(
        "2021-06-01 19:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 42) == pd.Timestamp(
        "2021-06-01 19:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 43) == pd.Timestamp(
        "2021-06-01 20:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 44) == pd.Timestamp(
        "2021-06-01 20:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 45) == pd.Timestamp(
        "2021-06-01 21:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 46) == pd.Timestamp(
        "2021-06-01 21:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 47) == pd.Timestamp(
        "2021-06-01 22:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 48) == pd.Timestamp(
        "2021-06-01 22:30"
    ).tz_localize("UTC")


def test_utc_from_settlement_date_long_day():
    settlement_date = "2020-10-25"
    assert helpers.utc_from_sp(settlement_date, 1) == pd.Timestamp(
        "2020-10-24 23:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 2) == pd.Timestamp(
        "2020-10-24 23:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 3) == pd.Timestamp(
        "2020-10-25 00:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 4) == pd.Timestamp(
        "2020-10-25 00:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 5) == pd.Timestamp(
        "2020-10-25 01:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 6) == pd.Timestamp(
        "2020-10-25 01:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 7) == pd.Timestamp(
        "2020-10-25 02:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 8) == pd.Timestamp(
        "2020-10-25 02:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 9) == pd.Timestamp(
        "2020-10-25 03:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 10) == pd.Timestamp(
        "2020-10-25 03:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 11) == pd.Timestamp(
        "2020-10-25 04:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 12) == pd.Timestamp(
        "2020-10-25 04:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 13) == pd.Timestamp(
        "2020-10-25 05:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 14) == pd.Timestamp(
        "2020-10-25 05:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 15) == pd.Timestamp(
        "2020-10-25 06:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 16) == pd.Timestamp(
        "2020-10-25 06:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 17) == pd.Timestamp(
        "2020-10-25 07:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 18) == pd.Timestamp(
        "2020-10-25 07:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 19) == pd.Timestamp(
        "2020-10-25 08:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 20) == pd.Timestamp(
        "2020-10-25 08:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 21) == pd.Timestamp(
        "2020-10-25 09:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 22) == pd.Timestamp(
        "2020-10-25 09:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 23) == pd.Timestamp(
        "2020-10-25 10:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 24) == pd.Timestamp(
        "2020-10-25 10:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 25) == pd.Timestamp(
        "2020-10-25 11:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 26) == pd.Timestamp(
        "2020-10-25 11:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 27) == pd.Timestamp(
        "2020-10-25 12:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 28) == pd.Timestamp(
        "2020-10-25 12:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 29) == pd.Timestamp(
        "2020-10-25 13:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 30) == pd.Timestamp(
        "2020-10-25 13:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 31) == pd.Timestamp(
        "2020-10-25 14:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 32) == pd.Timestamp(
        "2020-10-25 14:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 33) == pd.Timestamp(
        "2020-10-25 15:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 34) == pd.Timestamp(
        "2020-10-25 15:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 35) == pd.Timestamp(
        "2020-10-25 16:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 36) == pd.Timestamp(
        "2020-10-25 16:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 37) == pd.Timestamp(
        "2020-10-25 17:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 38) == pd.Timestamp(
        "2020-10-25 17:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 39) == pd.Timestamp(
        "2020-10-25 18:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 40) == pd.Timestamp(
        "2020-10-25 18:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 41) == pd.Timestamp(
        "2020-10-25 19:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 42) == pd.Timestamp(
        "2020-10-25 19:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 43) == pd.Timestamp(
        "2020-10-25 20:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 44) == pd.Timestamp(
        "2020-10-25 20:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 45) == pd.Timestamp(
        "2020-10-25 21:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 46) == pd.Timestamp(
        "2020-10-25 21:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 47) == pd.Timestamp(
        "2020-10-25 22:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 48) == pd.Timestamp(
        "2020-10-25 22:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 49) == pd.Timestamp(
        "2020-10-25 23:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 50) == pd.Timestamp(
        "2020-10-25 23:30"
    ).tz_localize("UTC")


def test_utc_from_settlement_date_short_day():
    settlement_date = "2021-03-28"
    assert helpers.utc_from_sp(settlement_date, 1) == pd.Timestamp(
        "2021-03-28 00:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 2) == pd.Timestamp(
        "2021-03-28 00:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 3) == pd.Timestamp(
        "2021-03-28 01:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 4) == pd.Timestamp(
        "2021-03-28 01:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 5) == pd.Timestamp(
        "2021-03-28 02:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 6) == pd.Timestamp(
        "2021-03-28 02:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 7) == pd.Timestamp(
        "2021-03-28 03:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 8) == pd.Timestamp(
        "2021-03-28 03:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 9) == pd.Timestamp(
        "2021-03-28 04:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 10) == pd.Timestamp(
        "2021-03-28 04:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 11) == pd.Timestamp(
        "2021-03-28 05:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 12) == pd.Timestamp(
        "2021-03-28 05:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 13) == pd.Timestamp(
        "2021-03-28 06:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 14) == pd.Timestamp(
        "2021-03-28 06:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 15) == pd.Timestamp(
        "2021-03-28 07:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 16) == pd.Timestamp(
        "2021-03-28 07:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 17) == pd.Timestamp(
        "2021-03-28 08:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 18) == pd.Timestamp(
        "2021-03-28 08:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 19) == pd.Timestamp(
        "2021-03-28 09:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 20) == pd.Timestamp(
        "2021-03-28 09:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 21) == pd.Timestamp(
        "2021-03-28 10:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 22) == pd.Timestamp(
        "2021-03-28 10:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 23) == pd.Timestamp(
        "2021-03-28 11:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 24) == pd.Timestamp(
        "2021-03-28 11:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 25) == pd.Timestamp(
        "2021-03-28 12:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 26) == pd.Timestamp(
        "2021-03-28 12:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 27) == pd.Timestamp(
        "2021-03-28 13:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 28) == pd.Timestamp(
        "2021-03-28 13:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 29) == pd.Timestamp(
        "2021-03-28 14:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 30) == pd.Timestamp(
        "2021-03-28 14:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 31) == pd.Timestamp(
        "2021-03-28 15:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 32) == pd.Timestamp(
        "2021-03-28 15:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 33) == pd.Timestamp(
        "2021-03-28 16:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 34) == pd.Timestamp(
        "2021-03-28 16:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 35) == pd.Timestamp(
        "2021-03-28 17:00"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 36) == pd.Timestamp(
        "2021-03-28 17:30"
    ).tz_localize("utc")
    assert helpers.utc_from_sp(settlement_date, 37) == pd.Timestamp(
        "2021-03-28 18:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 38) == pd.Timestamp(
        "2021-03-28 18:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 39) == pd.Timestamp(
        "2021-03-28 19:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 40) == pd.Timestamp(
        "2021-03-28 19:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 41) == pd.Timestamp(
        "2021-03-28 20:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 42) == pd.Timestamp(
        "2021-03-28 20:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 43) == pd.Timestamp(
        "2021-03-28 21:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 44) == pd.Timestamp(
        "2021-03-28 21:30"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 45) == pd.Timestamp(
        "2021-03-28 22:00"
    ).tz_localize("UTC")
    assert helpers.utc_from_sp(settlement_date, 46) == pd.Timestamp(
        "2021-03-28 22:30"
    ).tz_localize("UTC")
    with pytest.raises(Exception):
        print(helpers.utc_from_sp(settlement_date, 47))


def test_utc_from_sp_vectorised():
    df = pd.DataFrame(
        {
            "settlement_date": ["2021-03-01", "2021-03-01", "2021-03-01"],
            "sp": [1, 2, 3],
        }
    )
    df["expected"] = df.apply(
        lambda x: helpers.utc_from_sp(x["settlement_date"], x["sp"]), axis=1
    )
    print(df.expected)
    print(type(df.expected))
    result = helpers.utc_from_sp_vectorised(df["settlement_date"], df["sp"])
    print(result)
    print(type(result))
    assert df.expected.to_list() == result.to_list()
    pd.testing.assert_series_equal(df.expected, result, check_names=False)


def test_sp_from_timestamp_winter_london():
    """If the timestamp is given in London time,
    always expect settlement period to follow same convention.

    For non-clock-change days, SP1 starts at midnight, SP48 starts at 23:30

    For clock-change days, there with either be two hours from 1-2 (long day)
    or no hours from 1-2 (short day).

    This will throw and error, and is a good reason to avoid this timezone.

    However the timezone allows for 'intuitive' tests, given that the
    settlement periods are based around this time zone
    """
    settlement_date = "2021-03-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "Europe/London"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)


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
    settlement_date = "2021-06-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "Europe/London"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)


def test_sp_from_timestamp_long_day_london():
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
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "Europe/London"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    # for the long day, there are two one o'clock's
    # so this will return a pytz AmbiguousTimeError
    # this is why should always deal in UTC!
    with pytest.raises(pytz.exceptions.AmbiguousTimeError):
        ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
        helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    with pytest.raises(pytz.exceptions.AmbiguousTimeError):
        ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
        helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 49)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 50)


def test_sp_from_timestamp_short_day_london():
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
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    next_settlement_date_obj = settlement_date_obj + pd.Timedelta(days=1)
    tz = "Europe/London"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    # for the short day, there is no 1 o'clock, so this will error
    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
        assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    with pytest.raises(pytz.exceptions.NonExistentTimeError):
        ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
        assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)


def test_sp_from_timestamp_winter_utc():
    """For a normal (not clock-change) winter day,
    the times are equivalent to Europe/London
    """
    settlement_date = "2021-03-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "UTC"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)


def test_sp_from_timestamp_summer_utc():
    """For a normal (not clock-change) summer day,
    local London times are offset by 1 hour from UTC
    """
    # long/short days don't matter for this function because using ts input
    settlement_date = "2021-06-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    next_settlement_date_obj = settlement_date_obj + pd.Timedelta(days=1)
    tz = "UTC"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (next_settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (next_settlement_date_obj, 2)


def test_sp_from_timestamp_long_day_utc():
    """For a long clock change day,
    times start in the normal summertime mode (starting SP 3
    and run through to 50 (rather than restarting after 48)
    """
    # long/short days don't matter for this function because using utc input
    settlement_date = "2020-10-25"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "UTC"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 49)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 50)


def test_sp_from_timestamp_short_day_utc():
    """For a short clock change day,
    times start in the normal wintertime mode (starting SP 1)
    and restart after 46
    """
    settlement_date = "2021-03-28"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    next_settlement_date_obj = settlement_date_obj + pd.Timedelta(days=1)
    tz = "UTC"
    ts = pd.Timestamp(f"{settlement_date} 00:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 00:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    ts = pd.Timestamp(f"{settlement_date} 01:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = pd.Timestamp(f"{settlement_date} 01:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = pd.Timestamp(f"{settlement_date} 02:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = pd.Timestamp(f"{settlement_date} 02:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = pd.Timestamp(f"{settlement_date} 03:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = pd.Timestamp(f"{settlement_date} 03:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = pd.Timestamp(f"{settlement_date} 04:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = pd.Timestamp(f"{settlement_date} 04:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = pd.Timestamp(f"{settlement_date} 05:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = pd.Timestamp(f"{settlement_date} 05:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = pd.Timestamp(f"{settlement_date} 06:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = pd.Timestamp(f"{settlement_date} 06:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = pd.Timestamp(f"{settlement_date} 07:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = pd.Timestamp(f"{settlement_date} 07:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = pd.Timestamp(f"{settlement_date} 08:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = pd.Timestamp(f"{settlement_date} 08:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = pd.Timestamp(f"{settlement_date} 09:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = pd.Timestamp(f"{settlement_date} 09:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = pd.Timestamp(f"{settlement_date} 10:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = pd.Timestamp(f"{settlement_date} 10:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = pd.Timestamp(f"{settlement_date} 11:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = pd.Timestamp(f"{settlement_date} 11:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = pd.Timestamp(f"{settlement_date} 12:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = pd.Timestamp(f"{settlement_date} 12:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = pd.Timestamp(f"{settlement_date} 13:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = pd.Timestamp(f"{settlement_date} 13:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = pd.Timestamp(f"{settlement_date} 14:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = pd.Timestamp(f"{settlement_date} 14:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = pd.Timestamp(f"{settlement_date} 15:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = pd.Timestamp(f"{settlement_date} 15:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = pd.Timestamp(f"{settlement_date} 16:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = pd.Timestamp(f"{settlement_date} 16:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = pd.Timestamp(f"{settlement_date} 17:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = pd.Timestamp(f"{settlement_date} 17:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = pd.Timestamp(f"{settlement_date} 18:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = pd.Timestamp(f"{settlement_date} 18:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = pd.Timestamp(f"{settlement_date} 19:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = pd.Timestamp(f"{settlement_date} 19:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = pd.Timestamp(f"{settlement_date} 20:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = pd.Timestamp(f"{settlement_date} 20:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = pd.Timestamp(f"{settlement_date} 21:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = pd.Timestamp(f"{settlement_date} 21:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = pd.Timestamp(f"{settlement_date} 22:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = pd.Timestamp(f"{settlement_date} 22:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = pd.Timestamp(f"{settlement_date} 23:00").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (next_settlement_date_obj, 1)
    ts = pd.Timestamp(f"{settlement_date} 23:30").tz_localize(tz)
    assert helpers.sp_from_timestamp(ts) == (next_settlement_date_obj, 2)


def test_sp_from_timestamp_string():
    # long/short days don't matter for this function because using utc input
    settlement_date = "2021-03-01"
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    tz = "UTC"
    ts = f"{settlement_date}T00:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 1)
    ts = f"{settlement_date}T00:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 2)
    ts = f"{settlement_date}T01:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 3)
    ts = f"{settlement_date}T01:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 4)
    ts = f"{settlement_date}T02:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 5)
    ts = f"{settlement_date}T02:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 6)
    ts = f"{settlement_date}T03:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 7)
    ts = f"{settlement_date}T03:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 8)
    ts = f"{settlement_date}T04:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 9)
    ts = f"{settlement_date}T04:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 10)
    ts = f"{settlement_date}T05:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 11)
    ts = f"{settlement_date}T05:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 12)
    ts = f"{settlement_date}T06:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 13)
    ts = f"{settlement_date}T06:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 14)
    ts = f"{settlement_date}T07:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 15)
    ts = f"{settlement_date}T07:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 16)
    ts = f"{settlement_date}T08:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 17)
    ts = f"{settlement_date}T08:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 18)
    ts = f"{settlement_date}T09:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 19)
    ts = f"{settlement_date}T09:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 20)
    ts = f"{settlement_date}T10:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 21)
    ts = f"{settlement_date}T10:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 22)
    ts = f"{settlement_date}T11:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 23)
    ts = f"{settlement_date}T11:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 24)
    ts = f"{settlement_date}T12:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 25)
    ts = f"{settlement_date}T12:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 26)
    ts = f"{settlement_date}T13:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 27)
    ts = f"{settlement_date}T13:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 28)
    ts = f"{settlement_date}T14:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 29)
    ts = f"{settlement_date}T14:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 30)
    ts = f"{settlement_date}T15:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 31)
    ts = f"{settlement_date}T15:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 32)
    ts = f"{settlement_date}T16:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 33)
    ts = f"{settlement_date}T16:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 34)
    ts = f"{settlement_date}T17:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 35)
    ts = f"{settlement_date}T17:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 36)
    ts = f"{settlement_date}T18:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 37)
    ts = f"{settlement_date}T18:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 38)
    ts = f"{settlement_date}T19:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 39)
    ts = f"{settlement_date}T19:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 40)
    ts = f"{settlement_date}T20:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 41)
    ts = f"{settlement_date}T20:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 42)
    ts = f"{settlement_date}T21:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 43)
    ts = f"{settlement_date}T21:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 44)
    ts = f"{settlement_date}T22:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 45)
    ts = f"{settlement_date}T22:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 46)
    ts = f"{settlement_date}T23:00+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 47)
    ts = f"{settlement_date}T23:30+0000"
    assert helpers.sp_from_timestamp(ts) == (settlement_date_obj, 48)


@pytest.mark.parametrize(
    "settlement_date", ["2021-03-01", "2021-06-01", "2020-10-25", "2021-03-28"]
)
def test_sp_from_timestamp_winter_tz_naive(settlement_date):
    """For a naive timestamp, assume London local timezone"""
    settlement_date_ts = pd.Timestamp(settlement_date)
    settlement_date_obj = settlement_date_ts.date()
    naive = pd.Timestamp(f"{settlement_date} 00:00")
    assert helpers.sp_from_timestamp(naive) == helpers.sp_from_timestamp(
        naive.tz_localize("Europe/London")
    )
    naive = pd.Timestamp(f"{settlement_date} 00:30")
    assert helpers.sp_from_timestamp(naive) == helpers.sp_from_timestamp(
        naive.tz_localize("Europe/London")
    )
    naive = pd.Timestamp(f"{settlement_date} 01:00")
    naive = pd.Timestamp(f"{settlement_date} 23:00")
    assert helpers.sp_from_timestamp(naive) == helpers.sp_from_timestamp(
        naive.tz_localize("Europe/London")
    )
    naive = pd.Timestamp(f"{settlement_date} 23:30")
    assert helpers.sp_from_timestamp(naive) == helpers.sp_from_timestamp(
        naive.tz_localize("Europe/London")
    )
