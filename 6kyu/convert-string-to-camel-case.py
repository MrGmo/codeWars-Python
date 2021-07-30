import re

def to_camel_case(text):
    new_str = re.sub('[-_]', ' ', text).title().replace(' ', '')
    if len(text) == 0:
        return ''
    elif text[0] == text[0].upper():
        return new_str
    else:
        return new_str[0].lower() + new_str[1:]