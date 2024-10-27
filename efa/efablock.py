import pandas as pd

from efa.efaday import EFADay


class EFABlock:
    """Class to hold a specific EFA block for a given date and time."""

    def __init__(self, efa_date: EFADay, num: int):
        self.efa_date = EFADay(efa_date)
        self.delivery_date = self.efa_date.date
        self.num = num
        self.start_time = self.efa_date.start_time + pd.Timedelta(
            hours=4 * (self.num - 1)
        )
        self.end_time = self.start_time + pd.Timedelta(hours=4)
        self.is_wd = is_wd(self.delivery_date)
        self.is_we = is_we(self.delivery_date)
        self.name = self._make_name()

    def _make_name(self):
        if self.is_wd:
            return f"WD{self.num}"
        else:
            return f"WE{self.num}"

    def __str__(self):
        return f"{self.delivery_date} {self.name}"

    def __repr__(self):
        return f"EFABlock('{self.delivery_date}', {self.num})"

    def __eq__(self, other):
        return (self.efa_date == other.efa_date) & (self.num == other.num)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.efa_date < other.efa_date) | (
            (self.efa_date == other.efa_date) & (self.num < other.num)
        )

    def __le__(self, other):
        return self.__lt__(other) | self.__eq__(other)

    def __gt__(self, other):
        return (self.efa_date > other.efa_date) | (
            (self.efa_date == other.efa_date) & (self.num > other.num)
        )

    def __ge__(self, other):
        return self.__gt__(other) | self.__eq__(other)

    def __hash__(self):
        return hash((self.efa_date, self.num))

    def __add__(self, blocks: int):
        try:
            assert isinstance(blocks, int)
        except AssertionError:
            raise TypeError(
                "Only integer numbers of blocks can be added to an EFABlock object"
            )

        return EFABlock.from_start_time(
            self.start_time + pd.Timedelta(hours=4 * blocks)
        )

    def __sub__(self, days: int):
        try:
            assert isinstance(days, int)
        except AssertionError:
            raise TypeError(
                "Only integer numbers of blocks can be added to an EFABlock object"
            )
        return EFABlock.from_start_time(self.start_time - pd.Timedelta(days=4 * days))

    @property
    def is_peak(self):
        return (self.num in [3, 4, 5]) and self.is_wd

    @property
    def is_off_peak(self):
        return not self.is_peak

    @property
    def is_nt(self):
        return self.num in [1, 2]

    @property
    def is_6(self):
        return self.num == 6

    def from_start_time(start_time):
        """
        Create an integer 1-6 from a start time. This is an abbreviation for the efa block.

        Will likely want a fully fledged EFABlock class but this will do for now.
        """
        _start_time = pd.Timestamp(start_time)
        _efa_day = EFADay.from_start_time(_start_time)
        assert _start_time.tzinfo is not None
        local_time = _start_time.astimezone("Europe/London")
        if local_time.hour < 3:
            return EFABlock(_efa_day, 1)
        elif local_time.hour < 7:
            return EFABlock(_efa_day, 2)
        elif local_time.hour < 11:
            return EFABlock(_efa_day, 3)
        elif local_time.hour < 15:
            return EFABlock(_efa_day, 4)
        elif local_time.hour < 19:
            return EFABlock(_efa_day, 5)
        elif local_time.hour < 23:
            return EFABlock(_efa_day, 6)
        else:
            return EFABlock(_efa_day, 1)


def is_we(datelike):
    timestamp = pd.Timestamp(datelike)
    return timestamp.weekday() >= 5


def is_wd(datelike):
    timestamp = pd.Timestamp(datelike)
    return timestamp.weekday() < 5
