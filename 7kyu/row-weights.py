def row_weights(a):
    one = []
    two = []
    for i in range(len(a)):
        if i % 2 == 0:
            one.append(a[i])
        else:
            two.append(a[i])
    return (sum(one),sum(two))