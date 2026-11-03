def trib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return trib_recursive(n-1) + trib_recursive(n-2) + trib_recursive(n-3)

def trib_memo(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = trib_memo(n-1, memo) + trib_memo(n-2, memo) + trib_memo(n-3, memo)
    return memo[n]

def trib_loop(n):
    result = 0

    a = 0
    b = 1
    c = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        for i in range(1, n+1):
            a, b, c = b, c, (a+b+c)
        return a

tests = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 7),
    (6, 13),
    (7, 24),
    (10, 149),
    (25, 1389537),
]

for n, expected in tests:
    a = trib_recursive(n)
    b = trib_memo(n, {})
    c = trib_loop(n)
    ok = (a == expected and b == expected and c == expected)
    print("OK  " if ok else "FAIL", n, "->", a, b, c, "expected", expected)