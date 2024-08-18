import datetime as dt
from typing import Union

from efa import helpers


class EFADay:
    def __init__(self, date: Union[dt.date, str]) -> None:
        """Initialises an EFADay object for a given date.

        Parameters
        ----------

        date : The date of the EFA day, either as a date object or string in the format
        'YYYY-MM-DD'

        """
        try:
            self.date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        except TypeError:
            assert isinstance(date, dt.date) | isinstance(date, self.__class__)
            if isinstance(date, self.__class__):
                self.date = date.date
            if isinstance(date, dt.date):
                self.date = date

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def __repr__(self):
        return f"EFADay('{self.date.strftime('%Y-%m-%d')}')"

    def __eq__(self, other):
        try:
            return (self.date == other.date) & (self.__class__ == other.__class__)
        except AttributeError:
            return False

    def __ne__(self, other):
        return self.date != other

    def __lt__(self, other):
        return self.date < other

    def __le__(self, other):
        return self.date <= other

    def __gt__(self, other):
        return self.date > other

    def __ge__(self, other):
        return self.date >= other

    def __hash__(self):
        return hash(self.date)

    def __add__(self, days: int):
        try:
            assert isinstance(days, int)
        except AssertionError:
            raise TypeError("Only integer values can be added to an EFADay object")
        return EFADay(self.date + dt.timedelta(days=days))

    def __sub__(self, days: int):
        try:
            assert isinstance(days, int)
        except AssertionError:
            raise TypeError("Only integer values can be added to an EFADay object")
        return EFADay(self.date - dt.timedelta(days=days))

    @property
    def start_time(self) -> dt.datetime:
        """Returns UTC start time of the EFA day."""
        _prev_date = self.date - dt.timedelta(days=1)
        max_sp = helpers.max_sp(_prev_date)
        start_time = helpers.utc_from_sp(_prev_date, max_sp - 1)
        return start_time

    @property
    def end_time(self) -> dt.datetime:
        """Returns UTC end time of the EFA day."""
        max_sp = helpers.max_sp(self.date)
        end_time = helpers.utc_from_sp(self.date, max_sp - 1)
        return end_time

    @property
    def last_sp_start_time(self) -> dt.datetime:
        """Returns the last start time of the EFA day i.e. 22:30 local time"""
        return self.end_time - dt.timedelta(minutes=30)

    @property
    def gas_day(self) -> dt.datetime:
        """Returns the gas day bounday of the EFA day."""
        return self.end_time - dt.timedelta(hours=17)

    def from_period_start_time(start_time: dt.datetime) -> int:
        """Returns an EFA Day corresponding to a given utc start time."""
        settlement_date, sp = helpers.sp_from_timestamp(start_time)
        if sp <= 46:
            return EFADay(settlement_date)
        else:
            return EFADay(settlement_date) + 1
