import functools

def strong_enough( earthquake, age ):
    strength = 1000 * 0.99 ** age
    shockwave = functools.reduce(lambda x, y: x*y, [sum(i) for i in earthquake])
    if strength <= shockwave: return "Needs Reinforcement!"
    return "Safe!"