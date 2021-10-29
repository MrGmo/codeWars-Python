def createDict(keys,vals):
    result = {}
    new_vals = vals + ([None]*(len(keys)-len(vals)))
    for i in range(len(keys)):
        result[keys[i]] = new_vals[i]
    return result