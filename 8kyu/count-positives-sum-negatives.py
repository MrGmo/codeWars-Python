def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    positive_count = 0
    negative_sum = 0
    
    for num in arr:
        if num <= 0:
            negative_sum += num
        else:
            positive_count += 1
    return [positive_count, negative_sum]