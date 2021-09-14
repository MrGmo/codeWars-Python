def spoonerize(w):
    w = w.split()
    return w[1][0]+w[0][1:] + ' '+ w[0][0]+w[1][1:]