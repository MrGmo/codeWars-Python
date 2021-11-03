import re

def remove_vowels(string):
    return re.sub('[aeiou]', '', string)
    