import re

def valid_number(n):
    return True if re.match(r"[-+]?\d*\.(\d){2}$", n) else False
