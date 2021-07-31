def solution(s):
    result_str = s
    result = []
    if len(s) % 2 != 0:
        result_str += '_'
    for i in range(0,len(result_str),2):
        result.append(result_str[slice(i,i+2)])
    return result