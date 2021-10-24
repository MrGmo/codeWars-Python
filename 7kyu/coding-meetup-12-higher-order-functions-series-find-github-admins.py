def find_admin(lst, lang):
    result = []
    for obj in lst:
        if obj['language'] == lang and obj['githubAdmin'] == 'yes':
            result.append(obj)
    return result