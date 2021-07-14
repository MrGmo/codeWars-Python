def solution(num):
    if num < 0:
        return 0
    divs = []
    for i in range(1, num):
        if i % 15 == 0:
            divs.append(i)
            continue
        if i % 3 == 0:
            divs.append(i)
        if i % 5 == 0:
            divs.append(i)
    return sum(divs)