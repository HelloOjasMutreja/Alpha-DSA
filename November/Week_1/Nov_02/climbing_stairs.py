def climb_stairs(n):

    total = 0

    for x in range ((n//2) + 1):
        total += fact(n-x) // (fact(x) * fact(n-(2*x)))
    return total

def fact(f):
    if f == 0:
        return 1
    return f * fact(f - 1)

tests = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89),
]

for n, expected in tests:
    got = climb_stairs(n)
    print("OK  " if got == expected else "FAIL", n, "->", got, "expected", expected)