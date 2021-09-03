def find_screen_height(width, ratio):
    h_num = list(map(int,ratio.split(':')))[1]
    w_num = list(map(int,ratio.split(':')))[0]
    height = str(int(width*(h_num/w_num)))
    return f'{str(width)}x{height}'