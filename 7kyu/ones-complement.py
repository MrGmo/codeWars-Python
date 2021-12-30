def ones_complement(bin_num):
    return bin_num.translate(str.maketrans("10", "01"))
