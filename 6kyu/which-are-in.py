def in_array(array1, array2):
  res = []
  for a1 in array1:
    for a2 in array2:
      if a1 in a2 and not a1 in res:
        res.append(a1)
  res.sort()
  return res