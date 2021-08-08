def number(bus_stops):
    on_bus = 0
    for x,y in bus_stops:
        on_bus += x
        on_bus -= y
    return on_bus