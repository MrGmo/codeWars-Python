import math

def predict_age(*ages):
    return math.floor((sum([x**2 for x in ages])**(1/2))/2)