def format_poem(poem):
    p = poem.split('. ')
    result = ''
    for word in p:
        result += word + '.\n'
    return result[:-2]