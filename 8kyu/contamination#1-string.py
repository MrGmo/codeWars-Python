def contamination(text, char):
    if len(text) == 0 or len(char) == 0:
        return ''
    return char*len(text)