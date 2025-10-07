"""Vectorised helper functions taken from originals in utils/date_functions"""
from typing import Tuple, Union

import numpy as np
import pandas as pd


def _to_europe_london_tz(dates: pd.DatetimeIndex):
    try:
        ts = pd.to_datetime(dates).tz_localize("Europe/London")
    except TypeError:
        ts = pd.to_datetime(dates).tz_convert("Europe/London")
    return ts


def is_short_day(dates: pd.DatetimeIndex) -> np.ndarray:
    """Returns True if datechosen date is a short day, False if not

    Vectorised version of helpers.is_short_day

    Parameters
    ----------

    dates : Dates to check

    Returns
    -------

    np.ndarry of bools

    """
    ts = _to_europe_london_tz(dates)
    next_ts = ts + pd.Timedelta(days=1)
    return (ts.map(lambda x: x.dst()) == pd.Timedelta(hours=0)) & (
        next_ts.map(lambda x: x.dst()) == pd.Timedelta(hours=1)
    )


def is_long_day(date):
    """Returns True if datechosen date is a long day, False if not

    Vectorised version of helpers.is_long_day

    Parameters
    ----------

    dates : Dates to check

    Returns
    -------

    np.ndarry of bools

    """
    ts = _to_europe_london_tz(date)
    next_ts = ts + pd.Timedelta(days=1)
    return (ts.map(lambda x: x.dst()) == pd.Timedelta(hours=1)) & (
        next_ts.map(lambda x: x.dst()) == pd.Timedelta(hours=0)
    )


def max_sp(settlement_date):
    if is_long_day(settlement_date):
        return 50
    elif is_short_day(settlement_date):
        return 46
    else:
        return 48


def utc_from_sp(settlement_date: pd.Series, settlement_period: pd.Series):
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


def sp_from_timestamps(timestamps: pd.Series) -> Tuple[pd.Series, pd.Series]:
    """returns settlement period corresponding to a given time

    Timestamp can be any object that pandas will interpret e.g. a string or a pd.Timestamp,
    ideally in UTC

    If time is tz naive, it will be assumed to be Europe/London

    Parameters
    ----------

    timestamps : pd.Series of timestamps


    Returns
    -------

    Tuple of pd.Series of dates and pd.Series of settlement periods, each with the same
    index as the input

    Warning:
    --------
    While you can use a DST Timezone like Europe/London, this could error on clock change days.
    """
    try:
        london_timestamps = pd.to_datetime(timestamps).dt.tz_convert("Europe/London")
    except TypeError:
        london_timestamps = pd.to_datetime(timestamps).dt.tz_localize("Europe/London")
    settlement_dates = london_timestamps.dt.normalize()
    time_deltas = london_timestamps - settlement_dates
    half_hours = time_deltas.dt.total_seconds() / 1800
    settlement_periods = half_hours + 1
    # don't want timezone info on return settlement_dates
    settlement_dates = settlement_dates.dt.tz_localize(None)
    settlement_periods = settlement_periods.astype(int)
    return settlement_dates, settlement_periods


def efa_dates_from_timestamps(timestamps: pd.Series) -> pd.Series:
    """Returns the EFA date for each timestamp in the input series

    The EFA date is the date on which the EFA day starts. The EFA day starts at 23:00
    on the previous calendar day and runs to 23:00 on the calendar day shown as the
    EFA date.

    Parameters
    ----------

    timestamps : pd.Series of timestamps

    Returns
    -------

    pd.Series of EFA dates, each with the same index as the input

    Warning:
    --------
    While you can use a DST Timezone like Europe/London, this could error on clock change days.
    """
    settlement_dates, settlement_periods = sp_from_timestamps(timestamps)
    efa_dates = settlement_dates.where(
        settlement_periods <= 46, settlement_dates + pd.Timedelta(days=1)
    )
    return efa_dates
