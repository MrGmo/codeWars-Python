def whatday(num):
    obj = {
        1:'Sunday',
        2:'Monday',
        3:'Tuesday',
        4:'Wednesday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'
    }
    return obj.get(num, 'Wrong, please enter a number between 1 and 7')