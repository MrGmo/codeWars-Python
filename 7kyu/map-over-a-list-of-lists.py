def grid_map(inp, op):
    result = []
    for i in range(len(inp)):
        temp = []
        for j in range(len(inp[i])):
            temp.append(op(inp[i][j]))
        result.append(temp)
    return result
