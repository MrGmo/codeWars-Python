#Problem 1

def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result

#Problem 2
