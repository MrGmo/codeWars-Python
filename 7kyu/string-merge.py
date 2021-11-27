def string_merge(string1, string2, letter):
    s1_indx = string1.find(letter)
    s2_indx = string2.find(letter)
    return string1[:s1_indx]+string2[s2_indx:]
