def find_children(lst,child):
    result = []
    for name in lst:
        if name in child:
            result.append(name)
    return sorted(result)