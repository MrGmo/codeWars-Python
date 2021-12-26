def test(r):
    obj = {"h": 0, "a": 0, "l": 0}
    for num in r:
        if num in [9, 10]:
            obj["h"] += 1
        if num in [7, 8]:
            obj["a"] += 1
        if num in [1, 2, 3, 4, 5, 6]:
            obj["l"] += 1
    test_avg = round(sum(r) / len(r), 3)

    if all(num > 8 for num in r):
        return [test_avg, obj, "They did well"]
    return [test_avg, obj]
