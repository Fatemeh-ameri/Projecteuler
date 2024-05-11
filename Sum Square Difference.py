def Sum_Square_Difference(number):
    sum_of_squares = sum([i**2 for i in range(1, number+1)])
    square_of_sum = sum(range(1, number+1))**2
    return square_of_sum - sum_of_squares

print(Sum_Square_Difference(100))
#25164150