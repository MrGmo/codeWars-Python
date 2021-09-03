def encode(message,key):
    result= []
    key = str(key)
    while len(message) > len(key):
        for i in range(len(key)):
            key += key[i]
    for i in range(len(message)):
        result.append(ord(message[i])-96+int(key[i]))
    return result