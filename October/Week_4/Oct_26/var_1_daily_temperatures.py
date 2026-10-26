def next_greater_element(temps):

    stack = []
    next_greater = {}

    for i in range(len(temps)):
        while len(stack) > 0 and temps[i] > temps[stack[-1]]:
            next_greater[stack[-1]] = temps[i]
            stack.pop()    
        stack.append(i)
        print("i =", i, "stack =", stack, "dict =", next_greater)
    
    result = [0] * len(temps)

    for i in range(len(temps)):
        if temps[i] in next_greater:
            result.append(next_greater[temps[stack[i]]])
        else:
            result.append(-1)

    return result

tests = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([30, 20, 10], [0, 0, 0])
]

for temps, expected in tests:
    got = next_greater_element(temps)
    print("OK  " if got == expected else "FAIL", temps, "->", got, "expected")