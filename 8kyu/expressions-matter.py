def expression_matter(a, b, c):
    max_list = []
    max_list.append((a+b)*c)
    max_list.append(a*(b+c))
    max_list.append(a*b*c)
    max_list.append(a+b+c)
    return max(max_list)