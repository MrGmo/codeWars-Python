def find_squares(num):
  if num == 1:
    return '1-0'
  
  new_list = [x**2 for x in range(2, num)]

  for i in range(0, len(new_list)-1):
    if new_list[i+1]-new_list[i] == num:
      return f'{new_list[i+1]}-{new_list[i]}'