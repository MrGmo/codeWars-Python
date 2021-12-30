def vowel_one(s):
    result_str = ""
    for char in s:
        if char in "aeiouAEIOU":
            result_str += "1"
        else:
            result_str += "0"
    return result_str
