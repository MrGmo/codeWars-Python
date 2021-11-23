def solution(n,d):
    n = str(n)
    if d <= 0:
        return []
    return list(map(int,list(n[-d:])))