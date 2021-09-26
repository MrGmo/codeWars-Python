def mean(l):
    total = 0
    count = 0
    word = ''
    for char in l:
        if char.isalpha():
            word += char
        else:
            total += int(char)
            count +=1
    return [total/count,word]