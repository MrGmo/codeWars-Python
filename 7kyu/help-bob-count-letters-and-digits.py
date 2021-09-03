def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isdigit() or char.isalpha():
            count += 1
    return count