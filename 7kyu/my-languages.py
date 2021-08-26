def my_languages(r):
    result = []
    new_list = sorted(r.items(), key=lambda x: x[1])[::-1]
    for x in new_list:
        if x[1] > 59:
            result.append(x[0])
    return result