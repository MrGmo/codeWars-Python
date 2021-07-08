def define_suit(card):
    arr = ['clubs', 'diamonds', 'hearts', 'spades']
    if card[-1] == 'C':
        return arr[0]
    if card[-1] == 'D':
        return arr[1]
    if card[-1] == 'H':
        return arr[2]
    return arr[3]