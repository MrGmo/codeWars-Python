def last_survivor(let,coord):
    let = list(let)
    for num in coord:
        let.pop(num)
    return let[0]