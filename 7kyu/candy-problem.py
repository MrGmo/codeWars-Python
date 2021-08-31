def candies(s):
    if len(s) < 2:
        return -1
    return len(s)*max(s)-sum(s)