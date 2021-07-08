def toCsvText(array) :
   return '\n'.join(','.join(map(str, i)) for i in array)