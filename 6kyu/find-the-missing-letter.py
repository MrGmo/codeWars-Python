def find_missing_letter(c):
  for i in range(0,len(c)):
    current_num = ord(c[i])
    next_num = ord(c[i+1])
    if current_num+1 != next_num:
      return chr(current_num+1)
  return chr(ord(c[-1])+1)