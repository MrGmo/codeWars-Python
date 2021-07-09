def fillable(stock, merch, n):
    if merch in stock:
        if stock.get(merch) >= n:
            return True
    return False