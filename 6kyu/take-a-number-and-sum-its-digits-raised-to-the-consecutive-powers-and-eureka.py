def sum_dig_pow(a, b):
  result = []
  arr = list(range(a,b+1))
  for num in arr:
    if num_sum(num):
      result.append(num)
  return result

def num_sum(n):
  num_list = [int(x) for x in list(str(n))]
  length = len(num_list)
  count = 0
  for i in range(len(num_list)-1,-1,-1):
    count += num_list[i]**length
    length -= 1
  return count == n