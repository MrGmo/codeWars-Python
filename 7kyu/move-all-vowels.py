import re

def move_vowels(input):
    temp = ''
    for char in input:
        if char not in 'aeiou':
            temp += char
    for char in input:
        if char in 'aeiou':
            temp += char
    return temp
