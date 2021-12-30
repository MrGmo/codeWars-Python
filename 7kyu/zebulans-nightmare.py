def zebulans_nightmare(func):
    new_str = "".join(func.title().split("_"))
    return new_str[0].lower() + new_str[1:]
