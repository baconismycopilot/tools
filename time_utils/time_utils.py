"""
Speedlimit 88 MPH.
"""

from datetime import datetime


def is_valid_time(time_stamp: str) -> bool:
    """
    Verify time stamp is in a 12-hour format.

    :param time_stamp: :class:`str` 12-hour timestamp.

    :return: :class:`bool`
    """

    time_format = "%m/%d/%Y %I:%M %p"

    try:
        datetime.strptime(time_stamp, time_format)
    except ValueError:
        return False

    return True


def convert_from_epoch(epoch_time: int) -> str:
    """
    Return a 12-hour timestamp from EPOCH/UNIX time.

    :param epoch_time: EPOCH timestamp

    :return: :class:`str`
    """
    return datetime.fromtimestamp(epoch_time).strftime("%m/%d/%Y %I:%M %p")


def epoch_from_12_hour(special_ts: str) -> int:
    """
    Return an EPOCH timestamp from a 12-hour timestamp.

    :param special_ts: :class:`str`

    :return:
    """
    return int(datetime.strptime(special_ts, "%m/%d/%Y %I:%M %p").timestamp())


def in_the_past(time_stamp: int) -> bool:
    """
    Compare a timestamp to the current time.

    :param time_stamp: EPOCH timestamp

    :return: :class:`str`
    """
    return True if time_stamp < int(datetime.now().timestamp()) else False
