import re

def vowel_start(st):
    result_str = ""
    s = re.sub("[\W_+]", "", st).lower()
    for i in range(len(s)):
        if s[i] in "aeiou":
            result_str += " " + s[i]
        else:
            result_str += s[i]
    return result_str.strip()
