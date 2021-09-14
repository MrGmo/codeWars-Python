def outed(meet,boss):
    happy = 0
    peeps = 0
    for name, value in meet.items():
        if name == boss:
            happy += (2*value)
        else:
            happy += value
        peeps += 1
    return 'Get Out Now!'if happy/peeps <= 5 else 'Nice Work Champ!'