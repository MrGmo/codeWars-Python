def pattern(n):
    return "\n1".join("*" * i + str(i + 1) for i in range(n))