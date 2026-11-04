def is_power_of_two(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 != 0:
        return False
    else:
        x = 0
        while (n // 2**x) >= 1:
            if n == 2**x:
                return True
            else:
                x += 1
        return False

tests = [
    (1, True),
    (2, True),
    (3, False),
    (4, True),
    (6, False),
    (16, True),
    (0, False),
    (-8, False),
    (1024, True),
    (1023, False),
    (2147483648, True),
]

for n, expected in tests:
    got = is_power_of_two(n)
    print("OK  " if got == expected else "FAIL", n, "->", got, "expected", expected)