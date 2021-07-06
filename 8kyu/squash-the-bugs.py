def find_longest(string):
    spl = string.split(" ")
    
    longest = len(spl[0])

    for word in spl:
      if len(word) > longest:
        longest = len(word)
    return longest