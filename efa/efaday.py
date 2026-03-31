import datetime as dt
from typing import Union
from zoneinfo import ZoneInfo

import pandas as pd
from dateutil.relativedelta import relativedelta
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

    @property
    def year(self) -> int:
        return self.end_time.year

    @property
    def month(self) -> int:
        return self.end_time.month

    @property
    def day(self) -> int:
        return self.end_time.day

    @property
    def month_start(self) -> pd.Timestamp:
        start_date = dt.date(self.year, self.month, 1).strftime("%Y-%m-%d")
        return EFADay(start_date).start_time

    @property
    def month_end(self) -> pd.Timestamp:
        return self.month_start + relativedelta(months=1)

    @property
    def year_start(self) -> pd.Timestamp:
        start_date = dt.date(self.year, 1, 1).strftime("%Y-%m-%d")
        return EFADay(start_date).start_time

    @property
    def year_end(self) -> pd.Timestamp:
        return self.year_start + relativedelta(years=1)

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

    def efa_sp_from_utc(self, start_time):
        """Returns efa_sp from utc_start_time 1-48 (50)

        This is a 1-based count from the 2300 start time
        not the conventional settlement period.

        """
        if (start_time < self.start_time) or (start_time >= self.end_time):
            raise ValueError(
                f"start_time {start_time} for efa_sp_from_utc must be in efa day range for date {self}"
            )
        return (start_time - self.start_time).total_seconds() // 1800 + 1

    def make_hh_options(self):
        london = ZoneInfo("Europe/London")

        utc_times = list(self.start_time_index())
        gb_times = [t.astimezone(london) for t in utc_times]

        # First pass: plain HH:MM labels
        labels = [t.strftime("%H:%M") for t in gb_times]

        # Find duplicates (only happens on DST fallback day)
        duplicates = {l for l in labels if labels.count(l) > 1}

        options = []
        for utc_dt, gb_dt, label in zip(utc_times, gb_times, labels):
            if label in duplicates:
                label = gb_dt.strftime("%H:%M (%Z)")

            options.append(
                {
                    "label": label,
                    "value": utc_dt.isoformat(),
                }
            )

        return options
