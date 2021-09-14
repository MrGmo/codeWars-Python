def add(n1,n2):
    result = []
    n1 = list(map(int,list(str(n1))))
    n2 = list(map(int,list(str(n2))))
    
    while len(n1) > len(n2):
        n2.insert(0,0)
    while len(n1) < len(n2):
        n1.insert(0,0)
    
    for i in range(len(n1)-1,-1,-1):
        result.append(n1[i]+n2[i])
    
    return int(''.join(map(str,result[::-1])))