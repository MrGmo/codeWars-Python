def get_issuer(num):
    num = str(num)
    length = len(num)
    if length == 15 and num.startswith('34') or num.startswith('37'):
        return 'AMEX'
    if length == 16 and num.startswith('6011'):
        return 'Discover'
    if length == 16 and int(num[0]) == 5 and 0 < int(num[1]) < 6:
        return 'Mastercard'
    if length == 16 and num.startswith('4') or length == 13 and num.startswith('4'):
        return 'VISA'
    return 'Unknown'