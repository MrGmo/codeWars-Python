def is_same_language(lst):
    for i in range(len(lst)-1):
        lang1 = lst[i]['language']
        lang2 = lst[i+1]['language']
        if lang1 == lang2:
            pass
        else:
            return False
    return True