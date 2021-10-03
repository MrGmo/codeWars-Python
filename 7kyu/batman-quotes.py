import re

class BatmanQuotes(object):
  @staticmethod
  def get_quote(quotes, hero):
    return {'B':'Batman', 'R':'Robin', 'J':'Joker'}[hero[0]] + ": " + quotes[int(re.search('\d+', hero).group())]