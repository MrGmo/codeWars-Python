def update_light(current):
    colors = {
        'green':'yellow',
        'yellow':'red',
        'red':'green'
    }
    return colors.get(current)