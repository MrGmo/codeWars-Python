def sort_by_value_and_index(arr):
    result = []
    for i, val in enumerate(arr):
        result.append(((i + 1) * val, val))
    sorted_result = sorted(result, key=lambda x: x[0])
    return [x[1] for x in sorted_result]
