def evaporator(content,evap,threshold):
  start = content
  days = 0
  while start > content*(threshold/100):
    start -= (start*(evap/100))
    days += 1
  return days