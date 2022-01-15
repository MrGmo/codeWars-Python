def up_array(arr):
    a = ""
    b = []
    if len(arr) == 0:
        return None
    for i in arr:
        if i < 0 or i > 9:
            return None
        a = a + str(i)
    a = int(a) + 1
    for i in str(a):
        b.append(int(i))
    return b
