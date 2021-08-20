def is_letter(s):
    s = s.upper()
    if len(s) > 1 or len(s) == 0:
        return False
    return True if  91 > ord(s) > 64 else False