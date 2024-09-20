import pandas as pd

from efa.efaday import EFADay


class EFABlock:
    """Class to hold a specific EFA block for a given date and time."""

    def __init__(self, efa_date: EFADay, num: int):
        self.efa_date = EFADay(efa_date)
        self.delivery_date = efa_date.date
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
        _efa_day = EFADay.from_period_start_time(_start_time)
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
