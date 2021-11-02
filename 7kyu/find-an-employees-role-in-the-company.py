def find_employees_role(name):
    if ' ' not in name:
        return 'Does not work here!'
    first,last = name.split(' ')
    for employee in employees:
        if employee['first_name'] == first and employee['last_name'] == last:
            return employee['role']
    return 'Does not work here!'