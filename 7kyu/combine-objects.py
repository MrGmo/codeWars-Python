def combine(*dictionaries):
    result = {}
    for dict in dictionaries:
        for key, value in dict.items():
            result[key] = value + result.get(key, 0)
    return result
