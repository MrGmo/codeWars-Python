def excludingVatPrice(price):
    return round(price / 1.15, 2) if price else -1