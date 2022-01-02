from math import log, ceil
from datetime import datetime, date, timedelta

def date_nb_days(a0, a, p):
    start = datetime.strptime("2016-01-01", "%Y-%m-%d")
    r = ceil(log(a / float(a0)) / log(1 + p / 36000.0))
    return (start + timedelta(days=r)).strftime("%Y-%m-%d")
