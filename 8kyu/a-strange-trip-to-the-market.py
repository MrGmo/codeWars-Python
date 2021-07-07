def is_lock_ness_monster(string):
    words = ['three fifty', 'tree fiddy', '$3.50', '3.50']
    
    if any(x in string for x in words):
        return True
    else:
        return False