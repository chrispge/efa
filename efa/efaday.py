import datetime as dt
from typing import Union

import pandas as pd
from deprecated import deprecated

from efa import helpers


class EFADay:
    @classmethod
    @deprecated("Use from_start_time instead")
    def from_period_start_time(cls, start_time: dt.datetime):
        """Returns an EFA Day corresponding to a given utc start time."""
        settlement_date, sp = helpers.sp_from_timestamp(start_time)
        if sp <= 46:
            return cls(settlement_date)
        else:
            return cls(settlement_date) + 1

    @classmethod
    def from_start_time(cls, start_time: dt.datetime):
        """Returns an EFA Day corresponding to a given utc start time."""
        settlement_date, sp = helpers.sp_from_timestamp(start_time)
        if sp <= 46:
            return cls(settlement_date)
        else:
            return cls(settlement_date) + 1

    def __init__(self, date: Union[dt.date, str] = None) -> None:
        """Initialises an EFADay object for a given date.

        Parameters
        ----------

        date : The date of the EFA day, either as a date object or string in the format
        'YYYY-MM-DD'. If None, determines the EFA day based on current UTC time.

        """
        if date is None:
            date = self._get_current_date()
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
        # NB I use a comparison of Timestamps here to avoid the following warning:
        # In a future version these will be considered non-comparable. Use 'ts == pd.Timestamp(date)' or 'ts.date() == date' instead.
        try:
            return (pd.Timestamp(self.date) == pd.Timestamp(other.date)) & (
                self.__class__ == other.__class__
            )
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

    def start_time_index(self, freq: str = "30min", tz="utc") -> pd.DatetimeIndex:
        """Returns the hourly index of the EFA day."""
        return pd.Index(
            pd.date_range(
                self.start_time, self.end_time, freq=freq, inclusive="left"
            ).tz_convert(tz),
            name="start_time",
        )

    def start_time_from_utc_str(self, utc_str):
        """Returns a utc start_time from the utc_str e.g. '2300'"""
        hh = int(utc_str[:2])
        mm = int(utc_str[2:])
        if hh >= self.start_time.hour:
            base_date = self.date - dt.timedelta(days=1)
        else:
            base_date = self.date
        return dt.datetime(
            year=base_date.year,
            month=base_date.month,
            day=base_date.day,
            hour=hh,
            minute=mm,
            tzinfo=dt.timezone.utc,
        )

    def _get_current_date(self):
        utc_now = pd.Timestamp.utcnow()
        # conti dates are an hour ahead and syncronised with London changes
        # so easier to use those than add conditionals for 23:00 uk time
        conti_now = utc_now.tz_convert("Europe/Paris")
        return conti_now.date()
