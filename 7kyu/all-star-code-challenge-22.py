import math

def to_time(sec):
    hours = sec//3600
    mins = math.floor((sec-(hours*3600))/60)
    return f'{hours} hour(s) and {mins} minute(s)'