def eliminate_unset_bits(number):
    return int("0" + number.replace("0", ""), 2)
