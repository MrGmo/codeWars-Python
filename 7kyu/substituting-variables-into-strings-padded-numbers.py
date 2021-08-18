def solution(value):
    v = str(value)
    result = 'Value is '
    if len(v) < 5:
        result += '0'*(5-len(v))
    for char in v:
        result += char
    return result