def dative(word):
    result = word
    front = 'eéiíöőüű'
    back = 'aáoóuú'
    for i in range(len(word)-1,-1,-1):
        if word[i] in front:
            result += 'nek'
            break
        elif word[i] in back:
            result += 'nak'
            break
        else:
            pass
    return result