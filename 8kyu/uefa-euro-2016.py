def uefa_euro_2016(teams, scores):
    result = f'At match {teams[0]} - {teams[1]}, '
    if scores[0] > scores[1]:
        return result + f'{teams[0]} won!'
    elif scores[0] < scores[1]:
        return result + f'{teams[1]} won!'
    else:
        return result + 'teams played draw.'