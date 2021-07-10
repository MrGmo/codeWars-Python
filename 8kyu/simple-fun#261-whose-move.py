def whoseMove(lastPlayer, win):
    if win == True:
        return lastPlayer
    if lastPlayer == 'white' and win == False:
        return 'black'
    return 'white'