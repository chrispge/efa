import pandas as pd


def from_start_time(start_time) -> int:
    """
    Create an integer 1-6 from a start time. This is an abbreviation for the efa block.

    Will likely want a fully fledged EFABlock class but this will do for now.
    """
    _start_time = pd.Timestamp(start_time)
    assert _start_time.tzinfo is not None
    local_time = _start_time.astimezone("Europe/London")
    if local_time.hour < 3:
        return 1
    elif local_time.hour < 7:
        return 2
    elif local_time.hour < 11:
        return 3
    elif local_time.hour < 15:
        return 4
    elif local_time.hour < 19:
        return 5
    elif local_time.hour < 23:
        return 6
    else:
        return 1
