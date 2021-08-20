def solve(arr):
  count_arr = []
  for elem in arr:
    count = 0
    elem = elem.lower()
    for i in range(len(elem)):
      if ord(elem[i]) == i+97:
        count += 1
    count_arr.append(count)
  return count_arr