def digits(num):
    result = []
    n = list(map(int, list(str(num))))
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            result.append(n[i]+n[j])
    return result
