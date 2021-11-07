def histogram(r):
    return ''.join("{}|{}\n".format(len(r)-i, "" if not x else "{} {}".format("#" * x, x)) for i,x in enumerate(r[::-1]))