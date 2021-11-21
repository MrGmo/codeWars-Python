def word_to_bin(word):
    result = []
    for char in word:
        result.append('0'+bin(ord(char))[2:])
    return result