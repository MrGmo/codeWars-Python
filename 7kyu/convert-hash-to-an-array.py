def convert_hash_to_array(hash):
    result = []
    for v1,v2 in hash.items():
        result.append([v1,v2])
    return sorted(result)