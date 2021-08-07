def dont_give_me_five(start,end):
    arr = []
    for i in range(start,end+1):
        if str(5) in list(str(i)):
            pass
        else:
            arr.append(i)
    return len(arr)