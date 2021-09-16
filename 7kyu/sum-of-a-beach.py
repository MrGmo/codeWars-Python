def sum_of_a_beach(b):
    b = b.lower()
    arr = ['sand', 'water', 'fish', 'sun']
    count = []
    for elem in arr:
        count.append(b.count(elem))
    return sum(count)
    