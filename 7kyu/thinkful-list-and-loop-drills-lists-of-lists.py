def process_data(data):
    prod = 1
    for i in range(len(data)):
        prod *= data[i][0] - data[i][1]
    return prod
