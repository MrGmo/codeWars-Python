def reject(seq,pred):
    return [x for x in seq if pred(x) == False