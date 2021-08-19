def largest_pair_sum(numbers):
    max_sum = float('-inf')
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] > max_sum:
                max_sum = numbers[i] + numbers[j]
    return max_sum