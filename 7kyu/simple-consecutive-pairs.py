def pairs(arr):
    a = []
    count = 0
    for i in range(0,len(arr)-1,2):
        a.append((arr[i],arr[i+1]))
    for elem in a:
        if elem[0]+1 == elem[1] or elem[0]-1 == elem[1]:
            count += 1
    return count