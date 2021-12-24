def bald(s):
    count = s.count("/")
    s = s.replace("/", "")
    word = ""
    if count == 0:
        word = "Clean!"
    if count == 1:
        word = "Unicorn!"
    if count == 2:
        word = "Homer!"
    if count in [3, 4, 5]:
        word = "Careless!"
    if count > 5:
        word = "Hobo!"
    return ["-" * len(s) + "-" * count, word]
