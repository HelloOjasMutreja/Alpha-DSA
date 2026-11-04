def is_power_of_three(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 == 0:
        return False
    else:
        x = 0
        while (n // 3**x) >= 1:
            if n == 3**x:
                return True
            else:
                x += 1
        return False

tests = [
    (1, True),
    (3, True),
    (9, True),
    (27, True),
    (81, True),
    (0, False),
    (-3, False),
    (2, False),
    (6, False),
    (12, False),
    (45, False),
    (28, False),
    (26, False),
    (1162261467, True),
    (1162261468, False),
]

for n, expected in tests:
    got = is_power_of_three(n)
    print("OK  " if got == expected else "FAIL", n, "->", got, "expected", expected)