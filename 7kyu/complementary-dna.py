def DNA_strand(dna):
    obj = {
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
    }
    result = ''
    for char in dna:
        result += obj.get(char)
    return result