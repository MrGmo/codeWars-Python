def how_much_i_love_you(nb_petals):
    obj = {
        1:'I love you',
        2:'a little',
        3:'a lot',
        4:'passionately',
        5:'madly',
        0:'not at all'
    }

    if nb_petals < 6:
      return obj.get(nb_petals)
    else:
      return obj.get(nb_petals % 6)