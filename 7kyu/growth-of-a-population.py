import math

def nb_year(p0, percent, aug, p):
  count = p0
  numz = 0
  while count < p:
    count += math.floor((count*(percent/100))) + aug
    numz += 1
  return numz