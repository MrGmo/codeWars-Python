def add_letters(*letters):
    count = 0
    if len(letters) == 0:
        return 'z'
    for num in letters:
        count += ord(num)-96
    if count < 27:
        return chr(count+96)
    while count > 26:
        count -= 26
    return chr(count+96)