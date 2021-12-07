def countWins(winnerList, country):
    wins = 0
    for team in winnerList:
        if team["country"] == country:
            wins += 1
    return wins