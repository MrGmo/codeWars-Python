import math

def calculate_tip(amount, rating):
    rating = rating.lower()
    
    if rating == 'excellent':
        return math.ceil(amount*0.2)
    if rating == 'great':
        return math.ceil(amount*0.15)
    if rating == 'good':
        return math.ceil(amount*0.10)
    if rating == 'poor':
        return math.ceil(amount*0.05)
    if rating == 'terrible':
        return 0
    return 'Rating not recognised'