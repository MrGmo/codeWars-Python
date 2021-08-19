import math

def movie(card, ticket, perc):
    total = 0
    times = 1
    card_total = card
    t = ticket
    while total <= math.ceil(card_total):
      total += ticket
      card_total += (t*perc)
      t = t*perc
      times += 1
    return times-1