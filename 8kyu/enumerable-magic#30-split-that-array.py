def partition(arr, c_method):
    list1 = []
    list2 = []
    for elem in arr:
        if c_method(elem):
            list1.append(elem)
        else:
            list2.append(elem)
    return (list1, list2)