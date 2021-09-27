def nickname_generator(name):
    if len(name) < 4:
        return 'Error: Name too short'
    for i in range(len(name)):
        if name[2] not in 'aeiou':
            return name[:3]
        else:
            return name[:4]