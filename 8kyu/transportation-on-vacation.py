def rental_car_cost(d):
    if d > 6:
        return d*40 - 50
    if d > 2:
        return d*40 - 20
    return d*40