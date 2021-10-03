def bingo(arr):
    letters = []
    result = ''
    for num in arr:
        letters.append(chr(num+64))
    for char in letters:
        if char in 'BINGO':
            result += char
    sorted_bingo = ''.join(sorted(list(set(sorted(result)))))
    return 'WIN' if sorted_bingo == 'BGINO' else 'LOSE'