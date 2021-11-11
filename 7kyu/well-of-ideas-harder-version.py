def well(arr):
    new_list = [x.lower() for x in sum(arr, []) if type(x) == str]
    if new_list.count('good') > 2:
        return 'I smell a series!'
    if new_list.count('good') > 0:
        return 'Publish!'
    return 'Fail!'