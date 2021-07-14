def find_short(s):
    s = sorted(s.split())
    shorty = s[0]
    
    for word in s:
        if len(word) < len(shorty):
            shorty = word
    return len(shorty)