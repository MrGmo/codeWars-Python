def life_path_number(birthdate):
    b = birthdate.replace('-','')
    while len(b) > 1:
        total = sum([int(x) for x in list(b)])
        b = str(total)
    return total