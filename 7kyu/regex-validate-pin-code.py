import re

def validate_pin(pin):
    if len(pin) == 5 or len(pin) > 6:
        return False
    s = re.sub('[\D]', '', pin)
    if len(s) == 4 or len(s) == 6:
        return True
    return False