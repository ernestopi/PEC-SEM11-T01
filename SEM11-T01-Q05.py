if __name__ == "__main__":
    p = int(input())
    a = 1600
    original = p
    while (p >= 0.1 * original):
        n = 0.01 * p
        m = 0.06 * p
        p = p + n - m
        print(f'{a},{n:.0f},{m:.0f},{p:.0f}')
        a += 1

