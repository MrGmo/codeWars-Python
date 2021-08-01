def song_decoder(song):
  result = ''
  new_list = song.split('WUB')
  for word in new_list:
    if word.isalpha():
      result += word + ' '
  return result[:-1]