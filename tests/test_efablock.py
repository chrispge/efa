import datetime as dt

import pandas as pd
import pytest

from efa import EFABlock, EFADay


# Test EFABlock creation
def test_winter_block_1():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 1)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2020-12-31 23:00:00+00:00")
    assert block.num == 1
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD1"
    assert not block.is_peak
    assert block.is_off_peak


def test_winter_block_2():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 2)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2021-01-01 03:00:00+00:00")
    assert block.num == 2
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD2"
    assert not block.is_peak
    assert block.is_off_peak


def test_winter_block_3():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 3)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2021-01-01 07:00:00+00:00")
    assert block.num == 3
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD3"
    assert block.is_peak
    assert not block.is_off_peak


def test_winter_block_4():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 4)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2021-01-01 11:00:00+00:00")
    assert block.num == 4
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD4"
    assert block.is_peak
    assert not block.is_off_peak


def test_winter_block_5():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 5)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2021-01-01 15:00:00+00:00")
    assert block.num == 5
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD5"
    assert block.is_peak
    assert not block.is_off_peak


def test_winter_block_6():
    winter_date = EFADay("2021-01-01")
    block = EFABlock(winter_date, 6)
    assert block.efa_date == winter_date
    assert block.start_time == pd.Timestamp("2021-01-01 19:00:00+00:00")
    assert block.num == 6
    assert block.delivery_date == dt.date(2021, 1, 1)
    assert block.name == "WD6"
    assert not block.is_peak
    assert block.is_off_peak


def test_summer_block_1():
    summer_date = EFADay("2024-06-01")
    block = EFABlock(summer_date, 1)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2024-05-31 22:00:00+00:00")
    assert block.num == 1
    assert block.delivery_date == dt.date(2024, 6, 1)
    assert block.name == "WE1"


def test_summer_block_2():
    summer_date = EFADay("2024-06-01")
    block = EFABlock(summer_date, 2)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2024-06-01 02:00:00+00:00")
    assert block.num == 2
    assert block.delivery_date == dt.date(2024, 6, 1)
    assert block.name == "WE2"


def test_summer_block_3():
    summer_date = EFADay("2024-06-01")
    block = EFABlock(summer_date, 3)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2024-06-01 06:00:00+00:00")
    assert block.num == 3
    assert block.delivery_date == dt.date(2024, 6, 1)
    assert block.name == "WE3"


def test_summer_block_4():
    summer_date = EFADay("2021-06-01")
    block = EFABlock(summer_date, 4)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2021-06-01 10:00:00+00:00")
    assert block.num == 4
    assert block.delivery_date == dt.date(2021, 6, 1)
    assert block.name == "WD4"


def test_summer_block_5():
    summer_date = EFADay("2024-06-01")
    block = EFABlock(summer_date, 5)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2024-06-01 14:00:00+00:00")
    assert block.num == 5
    assert block.delivery_date == dt.date(2024, 6, 1)
    assert block.name == "WE5"


def test_summer_block_6():
    summer_date = EFADay("2024-06-01")
    block = EFABlock(summer_date, 6)
    assert block.efa_date == summer_date
    assert block.start_time == pd.Timestamp("2024-06-01 18:00:00+00:00")
    assert block.num == 6
    assert block.delivery_date == dt.date(2024, 6, 1)
    assert block.name == "WE6"


# Test EFABlock creation from start_time


def test_winter_00():
    winter_date = pd.Timestamp("2021-01-01 00:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 1


def test_winter_01():
    winter_date = pd.Timestamp("2021-01-01 01:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 1


def test_winter_02():
    winter_date = pd.Timestamp("2021-01-01 02:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 1


def test_winter_03():
    winter_date = pd.Timestamp("2021-01-01 03:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 2


def test_winter_04():
    winter_date = pd.Timestamp("2021-01-01 04:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 2


def test_winter_05():
    winter_date = pd.Timestamp("2021-01-01 05:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 2


def test_winter_06():
    winter_date = pd.Timestamp("2021-01-01 06:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 2


def test_winter_07():
    winter_date = pd.Timestamp("2021-01-01 07:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 3


def test_winter_08():
    winter_date = pd.Timestamp("2021-01-01 08:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 3


def test_winter_09():
    winter_date = pd.Timestamp("2021-01-01 09:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 3


def test_winter_10():
    winter_date = pd.Timestamp("2021-01-01 10:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 3


def test_winter_11():
    winter_date = pd.Timestamp("2021-01-01 11:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 4


def test_winter_12():
    winter_date = pd.Timestamp("2021-01-01 12:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 4


def test_winter_13():
    winter_date = pd.Timestamp("2021-01-01 13:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 4


def test_winter_14():
    winter_date = pd.Timestamp("2021-01-01 14:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 4


def test_winter_15():
    winter_date = pd.Timestamp("2021-01-01 15:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 5


def test_winter_16():
    winter_date = pd.Timestamp("2021-01-01 16:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 5


def test_winter_17():
    winter_date = pd.Timestamp("2021-01-01 17:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 5


def test_winter_18():
    winter_date = pd.Timestamp("2021-01-01 18:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 5


def test_winter_19():
    winter_date = pd.Timestamp("2021-01-01 19:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 6


def test_winter_20():
    winter_date = pd.Timestamp("2021-01-01 20:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 6


def test_winter_21():
    winter_date = pd.Timestamp("2021-01-01 21:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 6


def test_winter_22():
    winter_date = pd.Timestamp("2021-01-01 22:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 6


def test_winter_23():
    winter_date = pd.Timestamp("2021-01-01 23:00:00+00:00")
    result = EFABlock.from_start_time(winter_date)
    assert result.num == 1


# Summer times
def test_summer_00():
    summer_date = pd.Timestamp("2021-06-01 00:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 1


def test_summer_01():
    summer_date = pd.Timestamp("2021-06-01 01:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 1


def test_summer_02():
    summer_date = pd.Timestamp("2021-06-01 02:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 2


def test_summer_03():
    summer_date = pd.Timestamp("2021-06-01 03:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 2


def test_summer_04():
    summer_date = pd.Timestamp("2021-06-01 04:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 2


def test_summer_05():
    summer_date = pd.Timestamp("2021-06-01 05:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 2


def test_summer_06():
    summer_date = pd.Timestamp("2021-06-01 06:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 3


def test_summer_07():
    summer_date = pd.Timestamp("2021-06-01 07:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 3


def test_summer_08():
    summer_date = pd.Timestamp("2021-06-01 08:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 3


def test_summer_09():
    summer_date = pd.Timestamp("2021-06-01 09:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 3


def test_summer_10():
    summer_date = pd.Timestamp("2021-06-01 10:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 4


def test_summer_11():
    summer_date = pd.Timestamp("2021-06-01 11:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 4


def test_summer_12():
    summer_date = pd.Timestamp("2021-06-01 12:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 4


def test_summer_13():
    summer_date = pd.Timestamp("2021-06-01 13:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 4


def test_summer_14():
    summer_date = pd.Timestamp("2021-06-01 14:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 5


def test_summer_15():
    summer_date = pd.Timestamp("2021-06-01 15:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 5


def test_summer_16():
    summer_date = pd.Timestamp("2021-06-01 16:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 5


def test_summer_17():
    summer_date = pd.Timestamp("2021-06-01 17:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 5


def test_summer_18():
    summer_date = pd.Timestamp("2021-06-01 18:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 6


def test_summer_19():
    summer_date = pd.Timestamp("2021-06-01 19:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 6


def test_summer_20():
    summer_date = pd.Timestamp("2021-06-01 20:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 6


def test_summer_21():
    summer_date = pd.Timestamp("2021-06-01 21:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 6


def test_summer_22():
    summer_date = pd.Timestamp("2021-06-01 22:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 1


def test_summer_23():
    summer_date = pd.Timestamp("2021-06-01 23:00:00+00:00")
    result = EFABlock.from_start_time(summer_date)
    assert result.num == 1
