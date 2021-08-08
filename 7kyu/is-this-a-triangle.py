def is_triangle(a,b,c):
    sort_list = sorted([a,b,c])
    return sort_list[0] + sort_list[1] > sort_list[2]