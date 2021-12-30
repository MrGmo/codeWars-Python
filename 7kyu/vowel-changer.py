def vowel_change(txt, vow):
    return txt.translate(txt.maketrans("aeiouAEIOU", vow * 10))
