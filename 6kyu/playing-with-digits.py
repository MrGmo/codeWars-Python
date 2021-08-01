def dig_pow(n, p):
  num_list = [0]+ [int(x) for x in list(str(n))]
  powers_list = []
  for i in range(1,len(num_list)):
    powers_list.append(num_list[i]**(p+i-1))
  result = sum(powers_list)/n
  return int(result) if result.is_integer() else -1