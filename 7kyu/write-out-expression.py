def expression_out(exp):
    operator_dict = {
        "+": " Plus ",
        "-": " Minus ",
        "*": " Times ",
        "/": " Divided By ",
        "**": " To The Power Of ",
        "=": " Equals ",
        "!=": " Does Not Equal ",
    }
    nums = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
    }
    num1, oper, num2 = exp.split()
    if oper not in operator_dict:
        return "That's not an operator!"
    return nums.get(num1) + operator_dict.get(oper) + nums.get(num2)
