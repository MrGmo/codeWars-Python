def longest_word(string_of_words):
    s = string_of_words.split()
    long = s[0]
    for word in s:
        if len(word) >= len(long):
            long = word
    return long