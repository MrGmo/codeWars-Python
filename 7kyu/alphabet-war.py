def alphabet_war(fight):
    left_count = 0
    right_count = 0
    left = {
        'w':4,
        'p':3,
        'b':2,
        's':1
    }
    right = {
        'm':4,
        'q':3,
        'd':2,
        'z':1
    }
    
    for char in fight:
        if char in left:
            left_count += left.get(char)
        elif char in right:
            right_count += right.get(char)
        else:
            pass
    if right_count == left_count:
        return "Let's fight again!"
    elif right_count > left_count:
        return 'Right side wins!'
    else:
        return 'Left side wins!'