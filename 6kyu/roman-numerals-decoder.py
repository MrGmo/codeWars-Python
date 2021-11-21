def solution(roman):
    roman = roman.replace('CM', 'DCCCC').replace('CD','CCCC').replace('XC','LXXXX').replace('XL','XXXX').replace('IX','VIIII').replace('IV', 'IIII')
    num = 0
    roman_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    for char in roman:
        num += roman_dict.get(char)
    return num