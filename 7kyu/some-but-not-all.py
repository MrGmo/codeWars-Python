def some_but_not_all(seq, pred):
    return any(map(pred, seq)) and not all(map(pred, seq))