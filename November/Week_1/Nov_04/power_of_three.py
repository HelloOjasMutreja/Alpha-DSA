def is_power_of_three_loop(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n = n // 3
    return n == 1


def is_power_of_three_rec(n):
    if n == 1:
        return True
    elif n <= 0 or n % 2 == 0 or n % 3 != 0:
        return False
    else:
        return is_power_of_three_rec(n//3)


def is_power_of_three_max(n):
    # the largest power of three in 32-bit range is 3^19
    biggest = 1162261467

    if n <= 0:
        return False
    return biggest % n == 0


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
    a = is_power_of_three_loop(n)
    b = is_power_of_three_rec(n)
    c = is_power_of_three_max(n)
    ok = (a == expected and b == expected and c == expected)
    print("OK  " if ok else "FAIL", n, "->", a, b, c, "expected", expected)