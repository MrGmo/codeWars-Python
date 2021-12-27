def search(budget, prices):
    sorted_list = [str(x) for x in sorted([num for num in prices if num <= budget])]
    return ",".join(sorted_list) if len(sorted_list) > 0 else ""
