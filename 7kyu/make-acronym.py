def make_acronym(phrase):
    if type(phrase) != str:
        return "Not a string"
    if phrase.replace(" ", "").isalpha():
        return "".join([x[0].upper() for x in phrase.split()])
    return "Not letters" if len(phrase) > 0 else ""
