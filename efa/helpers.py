"""Helper functions taken from originals in utils/date_functions"""
import pandas as pd
from typing import Union


def _to_europe_london_tz(date):
    try:
        ts = pd.Timestamp(date).tz_localize("Europe/London")
    except TypeError:
        ts = pd.Timestamp(date).tz_convert("Europe/London")
    return ts


def is_short_day(date):
    ts = _to_europe_london_tz(date)
    next_ts = ts + pd.Timedelta(days=1)
    if ts.dst() == pd.Timedelta(hours=0) and next_ts.dst() == pd.Timedelta(hours=1):
        return True
    else:
        return False


def is_long_day(date):
    ts = _to_europe_london_tz(date)
    next_ts = ts + pd.Timedelta(days=1)
    if ts.dst() == pd.Timedelta(hours=1) and next_ts.dst() == pd.Timedelta(hours=0):
        return True
    else:
        return False


def max_sp(settlement_date):
    if is_long_day(settlement_date):
        return 50
    elif is_short_day(settlement_date):
        return 46
    else:
        return 48


def utc_from_sp(
    settlement_date: Union[pd.Timestamp, str], settlement_period: int
) -> pd.Timestamp:
    """Returns utc start time for settlement date / period combination

    Parameters
    ----------

    settlement_date : date-like
        Date of the settlement period

    settlement_period : int
        Settlement period

    Returns
    -------

    pd.Timestamp or pd.Series, depending on input

    See Also
    --------

    utc_from_sp_vectorised

    """
    assert settlement_period <= max_sp(settlement_date)
    midnight_local = pd.Timestamp(settlement_date).tz_localize("Europe/London")
    midnight_utc = midnight_local.tz_convert("UTC")
    time_delta = pd.Timedelta(hours=(int(settlement_period) - 1) / 2)
    return midnight_utc + time_delta


def utc_from_sp_vectorised(settlement_date: pd.Series, settlement_period: pd.Series):
    """Returns utc start time for settlement date / period combination

    Vectorised version of utc_from_sp

    Parameters
    ----------

    settlement_date : Series of date-like values
        Date of the settlement period

    settlement_period : Series of integer values
        Settlement period

    Returns
    -------

    pd.Timestamp or pd.Series, depending on input

    Notes
    -----

    Currently this function does NOT validate the input i.e. that the settlement period is valid for
    the given date. This is done in the non-vectorised version of this function.

    To fix this would require a vectorised version of max_sp, which in tern would require vectorised
    versions of is_long_day and is_short_day.

    See Also
    --------

    utc_from_sp

    """

    # assert settlement_period <= max_sp(settlement_date)
    midnight_local = pd.to_datetime(settlement_date).dt.tz_localize("Europe/London")
    midnight_utc = midnight_local.dt.tz_convert("UTC")
    time_delta = pd.to_timedelta((settlement_period - 1) / 2, unit="hours")
    return midnight_utc + time_delta


def sp_from_timestamp(timestamp):
    """returns settlement period corresponding to a given time

    Timestamp can be any object that pandas will interpret e.g. a string or a pd.Timestamp,
    ideally in UTC

    If time is tz naive, it will be assumed to be Europe/London

    Warning:
    --------
    While you can use a DST Timezone like Europe/London, this could error on clock change days.
    """
    try:
        london_timestamp = pd.Timestamp(timestamp).tz_convert("Europe/London")
    except TypeError:
        london_timestamp = pd.Timestamp(timestamp).tz_localize("Europe/London")
    settlement_date = london_timestamp.normalize()
    time_delta = london_timestamp - settlement_date
    half_hours = time_delta.total_seconds() / 1800
    settlement_period = half_hours + 1
    return settlement_date.date(), settlement_period
