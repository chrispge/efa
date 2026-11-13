import calendar
import datetime as dt
import warnings
from typing import Union
from zoneinfo import ZoneInfo

import pandas as pd
from dateutil.relativedelta import relativedelta
from deprecated import deprecated

from efa.period import LONDON, UTC, Period, _CalendarDay


class EFADay(_CalendarDay):
    @classmethod
    @deprecated("Use from_start_time instead")
    def from_period_start_time(cls, start_time: dt.datetime) -> "EFADay":
        """Returns an EFA Day corresponding to a given utc start time."""
        return cls.from_start_time(start_time)

    @classmethod
    def from_start_time(cls, start_time: dt.datetime) -> "EFADay":
        """Returns the EFA Day containing a given start time.

        Anything pandas reads as a timestamp is accepted. Naive input is read
        as Europe/London, which is deprecated: it will raise in 0.4.0.
        """
        ts = pd.Timestamp(start_time)
        if ts.tzinfo is None:
            warnings.warn(
                "naive start_time is read as Europe/London; pass a tz-aware "
                "time (naive input will raise in efa 0.4.0)",
                DeprecationWarning,
                stacklevel=2,
            )
            ts = ts.tz_localize("Europe/London")
        return cls(Period.containing(ts).efa_date)

    @classmethod
    def _start_of(cls, date: dt.date) -> dt.datetime:
        """UTC start of EFA date `date`: 23:00 London the evening before."""
        evening_before = date - dt.timedelta(days=1)
        return dt.datetime.combine(evening_before, dt.time(23), LONDON).astimezone(UTC)

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
    def start_time(self) -> pd.Timestamp:
        """Returns UTC start time of the EFA day."""
        # pd.Timestamp until 0.4.0, which returns the stdlib datetime
        return pd.Timestamp(self._start)

    @property
    def end_time(self) -> pd.Timestamp:
        """Returns UTC end time of the EFA day."""
        return pd.Timestamp(self._end)

    @property
    def last_sp_start_time(self) -> pd.Timestamp:
        """Returns the last start time of the EFA day i.e. 22:30 local time"""
        return self.end_time - dt.timedelta(minutes=30)

    @property
    def gas_day(self) -> pd.Timestamp:
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
        _, last_day = calendar.monthrange(self.year, self.month)
        # NB do not use relativedelta here - it gave wrong results
        return pd.Timestamp(
            year=self.year, month=self.month, day=last_day, hour=23, tz="Europe/London"
        ).tz_convert("UTC")

    @property
    def year_start(self) -> pd.Timestamp:
        start_date = dt.date(self.year, 1, 1).strftime("%Y-%m-%d")
        return EFADay(start_date).start_time

    @property
    def year_end(self) -> pd.Timestamp:
        return self.year_start + relativedelta(years=1)

    def start_time_index(
        self, freq: str = "30min", tz: str = "utc"
    ) -> pd.DatetimeIndex:
        """Returns the hourly index of the EFA day."""
        return pd.Index(
            pd.date_range(
                self.start_time, self.end_time, freq=freq, inclusive="left"
            ).tz_convert(tz),
            name="start_time",
        )

    def start_time_from_utc_str(self, utc_str) -> dt.datetime:
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

    def _get_current_date(self) -> dt.date:
        utc_now = pd.Timestamp.utcnow()
        # conti dates are an hour ahead and syncronised with London changes
        # so easier to use those than add conditionals for 23:00 uk time
        conti_now = utc_now.tz_convert("Europe/Paris")
        return conti_now.date()

    @deprecated("Use index(Period.containing(start_time)) instead")
    def efa_sp_from_utc(self, start_time) -> int:
        """Returns efa_sp from utc_start_time 1-48 (50)

        This is a 1-based count from the 2300 start time
        not the conventional settlement period.

        """
        period = Period.containing(start_time)
        if period not in self:
            raise ValueError(
                f"start_time {start_time} for efa_sp_from_utc must be in efa day range for date {self}"
            )
        return self.index(period)

    @property
    def max_efa_sp(self) -> int:
        return self.max_period

    @deprecated("Use period(efa_period).start_time instead")
    def utc_from_efa_sp(self, efa_sp: int) -> pd.Timestamp:
        """Returns utc_start_time from efa_sp"""
        if not isinstance(efa_sp, int):
            raise ValueError(f"efa_sp must be an integer, not {efa_sp}")
        if (efa_sp < 1) or (efa_sp > self.max_period):
            raise ValueError(
                f"efa_sp for {self} must be integer in range 1 to {self.max_period}."
            )
        return pd.Timestamp(self.period(efa_sp).start_time)

    def make_hh_options(self) -> list[dict[str, str]]:
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
                    "value": f"{self.index(Period(utc_dt)):02d}",
                }
            )

        return options
