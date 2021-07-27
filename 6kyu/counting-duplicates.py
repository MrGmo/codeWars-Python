def duplicate_count(text):
  s = text.lower()
  obj = {}
  for char in s:
    if char in obj:
      obj[char] += 1
    else:
      obj[char] = 1
  vals = list(obj.values())
  return len([x for x in vals if x > 1])