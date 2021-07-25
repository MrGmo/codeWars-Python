def divisors(integer):
    result = []
    for i in range(2, integer):
        if integer % i == 0:
            result.append(i)
    return f'{integer} is prime' if len(result) == 0 else result