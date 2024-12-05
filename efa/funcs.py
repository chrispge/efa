import pandas as pd

from efa.efaday import EFADay


def get_efa_days(
    start_time,
    end_time,
) -> list:
    """Returns list of EFADay objects which cover start_time and end_time

    Parameters
    ----------

    start_time : start time for seach of EFADay objects. Search is inclusive, is >= start_time
    end_time: end time for search of EFADay objects. Search is exclusive, is < end_time

    """
    first_date = EFADay.from_start_time(start_time).date
    # because end time search is exclusive (i.e. <) we need to go back 30 minutes
    _effective_end_time = pd.Timestamp(end_time) - pd.Timedelta(minutes=30)
    last_date = EFADay.from_start_time(_effective_end_time).date
    efa_dates = pd.date_range(start=first_date, end=last_date, freq="D")
    return [EFADay(efa_date) for efa_date in efa_dates]
