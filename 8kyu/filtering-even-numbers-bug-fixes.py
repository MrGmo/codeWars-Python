def kata_13_december(lst): 
    new = list()
    for i in range(len(lst)): 
        if lst[i] % 2 != 0: 
            new.append(lst[i])
    return new