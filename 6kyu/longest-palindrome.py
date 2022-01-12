def longest_palindrome(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            sub = s[j : j + i]
            if sub == sub[::-1]:
                return i
    return 0
