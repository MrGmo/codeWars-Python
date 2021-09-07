def solution(num):
    end = 0
    mid = 0
    start = 0
    for i in range(num):
        if i % 15 == 0:
            end += 1
        if i % 5 == 0 and i % 3 != 0:
            mid += 1
        if i % 3 == 0 and i % 5 != 0:
            start += 1 
    return [start, mid, end-1]