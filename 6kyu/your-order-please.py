import re

def order(s):
  s = s.split()
  fil = list(map(lambda x: re.sub('[^0-9]', '', x), s))
  results = {}
  final_str = ''
  for word in s:
    for char in fil:
      if char in word:
        results[int(char)] = word
  sorted_list = sorted(list(results.items()))

  for word in sorted_list:
    final_str += ' ' + word[1]
  return final_str[1:]