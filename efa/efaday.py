import datetime as dt
from efa import helpers
from typing import Union



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
            assert isinstance(date, dt.date)
            self.date = date

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

    def __repr__(self):
        return f"EFADay('{self.date.strftime('%Y-%m-%d')}')"

    def __eq__(self, other):
        try:
            return (self.date == other.date) & (self.__class__ == other.__class__)
        except AttributeError:
            return False

    def __ne__(self, other):
        return self.date != other.date

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __hash__(self):
        return hash(self.date)


    @property
    def start_time(self) -> dt.datetime:
        """Returns UTC start time of the EFA day."""
        _prev_date = self.date - dt.timedelta(days=1)
        max_sp = helpers.max_sp(_prev_date)
        start_time = helpers.utc_from_sp(_prev_date, max_sp-1)
        return start_time

    @property
    def end_time(self) -> dt.datetime:
        """Returns UTC end time of the EFA day."""
        max_sp = helpers.max_sp(self.date)
        end_time = helpers.utc_from_sp(self.date, max_sp-1)
        return end_time
