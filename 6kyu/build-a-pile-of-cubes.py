def find_nb(m):
  total = 0
  i = 1
  while total <= m:
    total += (i**3)
    i += 1
    if total == m:
      return i-1
  return -1