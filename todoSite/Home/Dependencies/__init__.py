import time
import datetime


def checkFormAddTime(deadline) -> bool:
    return time.mktime(datetime.datetime.strptime(deadline, "%Y-%m-%d").timetuple()) > int(time.time())