def order_word(s):
    if s == None or s == '':
        return 'Invalid String!'
    arr = [ord(x) for x in list(s)]
    return ''.join([chr(x) for x in sorted(arr)])