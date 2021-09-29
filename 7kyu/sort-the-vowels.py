def sort_vowels(s):
    try:
        return '\n'.join('|' + i  if i.lower() in 'aioue' else i + '|' for i in s)
    except:
        return ''