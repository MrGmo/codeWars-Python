def get_larger_numbers(a, b):
    new_array = []
    for i in range(len(a)):
        if a[i] > b[i]:
            new_array.append(a[i])
        else:
            new_array.append(b[i])
    return new_array