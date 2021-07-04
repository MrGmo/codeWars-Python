def bmi(weight, height):
    bmi_number = weight/(height**2)
    
    if bmi_number <= 18.5:
        return "Underweight"
    elif bmi_number <= 25.0:
        return "Normal"
    elif bmi_number <= 30.0:
        return "Overweight"
    else:
        return "Obese"