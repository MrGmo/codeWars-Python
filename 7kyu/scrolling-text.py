def scrolling_text(text):
    text = text.upper()
    texts = []
    for char in text:
        texts.append(text)
        text = text[1:] + text[0]
    return texts
