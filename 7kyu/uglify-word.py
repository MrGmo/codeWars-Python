def uglify_word(s):
    flag = 1
    answer = ""
    for c in s:
        if c.isalpha():
            answer += c.upper() if flag else c.lower()
            flag = 1 - flag
        else:
            answer += c
            flag = 1
    return answer
