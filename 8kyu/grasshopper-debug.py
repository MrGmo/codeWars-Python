def weather_info(temp):
    c = convert(temp)
    if c <= 0:
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert(temp):
    return (temp - 32) * (5/9)