def goto(level,button):
    levels = [0, 1, 2, 3]
    buttons = ['0', '1', '2', '3']
    if level not in levels or button not in buttons:
        return 0
    else:
        return int(button) - level