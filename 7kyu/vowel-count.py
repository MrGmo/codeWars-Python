def get_count(input_str):
    num_vowels = 0
    for char in input_str:
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels