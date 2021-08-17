def vowel_indices(word):
    result = []
    for i in range(len(word)):
        if word[i] in 'aeiouyAEIOUY':
            result.append(i+1)
    return result