def get_first_python(users):
    result = ''
    for elem in users:
        first = elem["first_name"]
        country = elem["country"]
        lang = elem["language"]
        if lang == "Python":
            result += first + ', ' + country
            break
    return result if len(result) > 0 else 'There will be no Python developers'