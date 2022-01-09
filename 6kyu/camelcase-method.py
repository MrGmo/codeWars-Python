def camel_case(string):
    s = string.strip()
    if len(s) == 0:
        return ""
    return "".join(x[0].upper() + x[1:] for x in s.split(" "))
