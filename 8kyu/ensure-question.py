def ensure_question(s):
    if len(s) == 0:
        return '?'
    if s[-1] == '?':
        return s
    return s + '?'