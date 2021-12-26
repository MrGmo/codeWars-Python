def fix(paragraph):
    result = ""
    p = paragraph.split(". ")
    for i in range(len(p)):
        result += p[i].capitalize() + ". "
    return result[:-2]
