def golf_score_calculator(par_string, score_string):
    par = 0
    for i in range(len(par_string)):
        par += (int(par_string[i])-int(score_string[i]))
    return par*-1