def matrix(arr):
  start = 0
  for i in range(start, len(arr)):
    if arr[i][i] < 0:
      arr[i][i] = 0
    else:
      arr[i][i] = 1
    start += 1
    continue
  return arr