def computer_to_phone(nums):
    result_str = ''
    convert_dict = {
        '7': '1',
        '8': '2',
        '9': '3',
        '1': '7',
        '2': '8',
        '3': '9'
    }
    for char in nums:
        result_str += convert_dict.get(char, char)
    return result_str