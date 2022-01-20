def insurance(age, size, num_of_days):
    if num_of_days <= 0:
        return 0
    cost = 0
    one_day_cost = 50
    if size == "medium":
        one_day_cost += 10
    elif size != "economy":
        one_day_cost += 15
    if age < 25:
        one_day_cost += 10
    cost = one_day_cost * num_of_days
    return cost
