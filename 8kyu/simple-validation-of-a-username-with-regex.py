import re

def validate_usr(username):
    is_right_length = False
    is_right_chars = False
    
    if len(username) > 3 and len(username) < 17:
        is_right_length = True
        
    new_str = re.sub("[^a-z0-9_]", '', username)
    
    if len(username) == len(new_str):
        is_right_chars = True
    
    return True if is_right_length and is_right_chars else False