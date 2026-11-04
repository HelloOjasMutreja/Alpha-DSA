def is_power_of_four(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 != 0:
        return False
    else:
        x = 0
        while (n // 4**x) >= 1:
            if n == 4**x:
                return True
            else:
                x += 1
        return False

tests = [
    (1, True),
    (4, True),
    (16, True),
    (64, True),
    (256, True),
    (0, False),
    (-4, False),
    (2, False),
    (8, False),
    (32, False),
    (5, False),
    (12, False),
    (15, False),
    (1073741824, True),
    (2147483648, False),
]

for n, expected in tests:
    got = is_power_of_four(n)
    print("OK  " if got == expected else "FAIL", n, "->", got, "expected", expected)