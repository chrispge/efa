import datetime as dt

import pandas as pd
import pytest

from efa.efablock import from_start_time


def test_winter_00():
    winter_date = pd.Timestamp("2021-01-01 00:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 1


def test_winter_01():
    winter_date = pd.Timestamp("2021-01-01 01:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 1


def test_winter_02():
    winter_date = pd.Timestamp("2021-01-01 02:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 1


def test_winter_03():
    winter_date = pd.Timestamp("2021-01-01 03:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 2


def test_winter_04():
    winter_date = pd.Timestamp("2021-01-01 04:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 2


def test_winter_05():
    winter_date = pd.Timestamp("2021-01-01 05:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 2


def test_winter_06():
    winter_date = pd.Timestamp("2021-01-01 06:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 2


def test_winter_07():
    winter_date = pd.Timestamp("2021-01-01 07:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 3


def test_winter_08():
    winter_date = pd.Timestamp("2021-01-01 08:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 3


def test_winter_09():
    winter_date = pd.Timestamp("2021-01-01 09:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 3


def test_winter_10():
    winter_date = pd.Timestamp("2021-01-01 10:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 3


def test_winter_11():
    winter_date = pd.Timestamp("2021-01-01 11:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 4


def test_winter_12():
    winter_date = pd.Timestamp("2021-01-01 12:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 4


def test_winter_13():
    winter_date = pd.Timestamp("2021-01-01 13:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 4


def test_winter_14():
    winter_date = pd.Timestamp("2021-01-01 14:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 4


def test_winter_15():
    winter_date = pd.Timestamp("2021-01-01 15:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 5


def test_winter_16():
    winter_date = pd.Timestamp("2021-01-01 16:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 5


def test_winter_17():
    winter_date = pd.Timestamp("2021-01-01 17:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 5


def test_winter_18():
    winter_date = pd.Timestamp("2021-01-01 18:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 5


def test_winter_19():
    winter_date = pd.Timestamp("2021-01-01 19:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 6


def test_winter_20():
    winter_date = pd.Timestamp("2021-01-01 20:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 6


def test_winter_21():
    winter_date = pd.Timestamp("2021-01-01 21:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 6


def test_winter_22():
    winter_date = pd.Timestamp("2021-01-01 22:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 6


def test_winter_23():
    winter_date = pd.Timestamp("2021-01-01 23:00:00+00:00")
    result = from_start_time(winter_date)
    assert result == 1


# Summer times
def test_summer_00():
    summer_date = pd.Timestamp("2021-06-01 00:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 1


def test_summer_01():
    summer_date = pd.Timestamp("2021-06-01 01:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 1


def test_summer_02():
    summer_date = pd.Timestamp("2021-06-01 02:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 2


def test_summer_03():
    summer_date = pd.Timestamp("2021-06-01 03:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 2


def test_summer_04():
    summer_date = pd.Timestamp("2021-06-01 04:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 2


def test_summer_05():
    summer_date = pd.Timestamp("2021-06-01 05:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 2


def test_summer_06():
    summer_date = pd.Timestamp("2021-06-01 06:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 3


def test_summer_07():
    summer_date = pd.Timestamp("2021-06-01 07:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 3


def test_summer_08():
    summer_date = pd.Timestamp("2021-06-01 08:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 3


def test_summer_09():
    summer_date = pd.Timestamp("2021-06-01 09:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 3


def test_summer_10():
    summer_date = pd.Timestamp("2021-06-01 10:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 4


def test_summer_11():
    summer_date = pd.Timestamp("2021-06-01 11:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 4


def test_summer_12():
    summer_date = pd.Timestamp("2021-06-01 12:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 4


def test_summer_13():
    summer_date = pd.Timestamp("2021-06-01 13:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 4


def test_summer_14():
    summer_date = pd.Timestamp("2021-06-01 14:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 5


def test_summer_15():
    summer_date = pd.Timestamp("2021-06-01 15:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 5


def test_summer_16():
    summer_date = pd.Timestamp("2021-06-01 16:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 5


def test_summer_17():
    summer_date = pd.Timestamp("2021-06-01 17:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 5


def test_summer_18():
    summer_date = pd.Timestamp("2021-06-01 18:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 6


def test_summer_19():
    summer_date = pd.Timestamp("2021-06-01 19:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 6


def test_summer_20():
    summer_date = pd.Timestamp("2021-06-01 20:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 6


def test_summer_21():
    summer_date = pd.Timestamp("2021-06-01 21:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 6


def test_summer_22():
    summer_date = pd.Timestamp("2021-06-01 22:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 1


def test_summer_23():
    summer_date = pd.Timestamp("2021-06-01 23:00:00+00:00")
    result = from_start_time(summer_date)
    assert result == 1
