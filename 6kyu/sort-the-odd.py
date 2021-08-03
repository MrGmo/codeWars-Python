def sort_array(arr):
  odds = []
  for num in arr:
    if num % 2 != 0:
      odds.append(num)
  sorted_odds = sorted(odds)

  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      sorted_odds.insert(i,arr[i])
  return sorted_odds