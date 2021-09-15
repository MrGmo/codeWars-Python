def replace_nth(text, n, old, new):
    count = 0
    res = ""
    for c in text:
        if c == old: 
            count += 1
            if count == n:
                res += new
                count = 0
                continue
        res += c
    return res