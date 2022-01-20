def pattern(n):
    return "\n".join("".join(str((d + i) % n + 1) for d in range(n)) for i in range(n))
