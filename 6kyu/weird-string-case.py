def to_weird_case(string):
    newstring = ''
    i = True
    for char in string:
        if i == True:
            newstring += char.upper()
            i = False
        if i == False:
            newstring += char.lower()
            i = True
        if char == " ":
            newstring += ""
            i = True
    return newstring