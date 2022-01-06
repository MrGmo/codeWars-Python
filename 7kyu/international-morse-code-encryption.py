def encryption(string):
    return " ".join(CHAR_TO_MORSE.get(a, a) for a in string)
