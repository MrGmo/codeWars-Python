def grid(N):
    s = "abcdefghijklmnopqrstuvwxyz"
    return (
        None
        if N < 0
        else "\n".join(" ".join(s[(i + j) % 26] for j in range(N)) for i in range(N))
    )
