def task(w,n,c):
    obj = {
        'Monday': 'James',
        'Tuesday': 'John',
        'Wednesday': 'Robert',
        'Thursday': 'Michael',
        'Friday': 'William'
    }
    return f'It is {w} today, {obj.get(w)}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'