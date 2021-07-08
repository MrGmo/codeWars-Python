def elevator(left, right, call):
    if left == right and right == left:
        return 'right'
    if left == call:
        return 'left'
    if abs(left-call) < abs(right-call):
        return 'left'
    return 'right'