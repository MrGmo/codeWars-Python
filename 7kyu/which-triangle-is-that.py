def type_of_triangle(*s):
    for num in s:
        if type(num) != int:
            return 'Not a valid triangle'
    s = sorted(s)

    if s[0]+s[1] < s[2]:
        return 'Not a valid triangle'
    if s[0] == s[1] == s[2]:
        return 'Equilateral'
    if len(set(s)) == 2:
        return 'Isosceles'
    return 'Scalene'