def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memo(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_loop(n):
    result = 0

    a = 0
    b = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n+1):
            a, b = b, (a+b)
        return a
    
tests = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (10, 55),
    (20, 6765),
]

for n, expected in tests:
    a = fib_recursive(n)
    b = fib_memo(n, {})
    c = fib_loop(n)
    ok = (a == expected and b == expected and c == expected)
    print("OK  " if ok else "FAIL", n, "->", a, b, c, "expected", expected)