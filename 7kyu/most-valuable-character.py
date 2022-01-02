def solve(st):
    seen_index = {}
    result = []
    if len(st) == 1:
        return st
    if len(set(st)) == len(st):
        return st[0]
    for i in range(len(st)):
        if st[i] not in seen_index:
            seen_index[st[i]] = [i]
        else:
            seen_index[st[i]].append(i)
    for key, val in seen_index.items():
        seen_index[key] = val[-1] - val[0]
    max_char, max_val = max(
        [(key, val) for key, val in seen_index.items()], key=lambda x: x[1]
    )
    for key, val in seen_index.items():
        if val == max_val:
            result.append(key)
    return sorted(result)[0]
