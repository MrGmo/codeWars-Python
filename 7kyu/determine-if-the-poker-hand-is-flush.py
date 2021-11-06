def is_flush(cards):
    return all(elem[-1] == cards[0][-1:] for elem in cards)