def tribonacci(sig,n):
    result_list = [*sig]
    if n == 0:
        return []
    if n <= 3:
        return sig[slice(0,n)]
    for i in range(3,n):
        next_num = result_list[-1] + result_list[-2] + result_list[-3]
        result_list.append(next_num)
    return result_list