def words_to_marks(s):
    count = 0
    for char in s:
        count += ord(char)-96
    return count