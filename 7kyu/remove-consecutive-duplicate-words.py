def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)