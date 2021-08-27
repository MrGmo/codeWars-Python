def pluck(o,n):
    result = []
    for elem in o:
        for key,val in elem.items():
            if key == n:
                result.append(val)
        if n not in elem:
            result.append(None)
    return result