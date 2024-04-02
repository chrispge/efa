"""Helper functions taken from originals in utils/date_functions"""
import pandas as pd

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

def utc_from_sp(settlement_date, settlement_period):
    """Use df.apply(lambda x: start_time_from_sp(x), axis=1)"""
    assert settlement_period <= max_sp(settlement_date)
    midnight_local = pd.Timestamp(settlement_date).tz_localize("Europe/London")
    midnight_utc = midnight_local.astimezone("UTC")
    return midnight_utc + pd.Timedelta(hours=(int(settlement_period) - 1) / 2)

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
