def search_names(logins):
    result = []
    for elem in logins:
        if '_' in elem[0]:
            result.append(elem)
    return result