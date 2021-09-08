from functools import reduce 

def difference_of_squares(n):
    square_sum = reduce(lambda x,y: x+y, range(1,n+1))**2
    sum_of_squares = 0
    for i in range(1,n+1):
        sum_of_squares += (i**2)
    return square_sum-sum_of_squares