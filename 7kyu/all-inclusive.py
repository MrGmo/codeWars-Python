def contain_all_rots(st, arr):
    if len(st) == 0:
        return True
    a = []
    for i in range(len(st)):
        st = list(st)
        last = st.pop()
        st.insert(0,last)
        a.append(''.join(st))
    
    for elem in a:
        if elem in arr:
            pass
        else:
            return False
    return True