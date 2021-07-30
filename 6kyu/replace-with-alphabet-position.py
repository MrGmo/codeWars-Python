def alphabet_position(text):
    result = ''
    for char in text:
        if char.isalpha() and char == char.upper():
            result += str(ord(char)-64) + ' '
        elif char.isalpha() and char == char.lower():
            result += str(ord(char)-96) + ' '
        else:
          pass
    return result[:-1]