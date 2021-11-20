import math

def number_property(n):
  return [is_prime(n), n % 2 == 0, n % 10 == 0]

def is_prime(n):
  if n % 2 == 0 and n > 2 or n < 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))