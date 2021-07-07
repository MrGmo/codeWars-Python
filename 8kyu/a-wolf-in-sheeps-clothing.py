def warn_the_sheep(q):
    new_list = q[::-1]
    index = new_list.index('wolf')
    
    if index == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return f'Oi! Sheep number {index}! You are about to be eaten by a wolf!'