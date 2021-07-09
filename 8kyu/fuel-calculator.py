def fuel_price(litres, ppl):
    if litres < 2:
        return litres*ppl
    if litres < 4:
        return litres*(ppl-0.05)
    if litres < 6:
        return litres*(ppl-0.10)
    if litres < 8:
        return litres*(ppl-0.15)
    if litres < 10:
        return litres*(ppl-0.20)
    return litres*(ppl-0.25)