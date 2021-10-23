def pendulum(a):
    a = sorted(a)
    return a[::2][::-1] + a[1::2]