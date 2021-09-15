def boredom(staff):
    score = 0
    arr = []
    obj = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    for key,value in staff.items():
        arr.append(value)
    for elem in arr:
        score += obj.get(elem)
    if score <= 80:
        return 'kill me now'
    if 80 < score < 100:
        return 'i can handle this'
    return 'party time!!'