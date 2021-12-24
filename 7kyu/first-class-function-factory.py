def factory(x):
    def some(array):
        new = []
        for i in array:
            new.append(i * x)
        return new
    return some
