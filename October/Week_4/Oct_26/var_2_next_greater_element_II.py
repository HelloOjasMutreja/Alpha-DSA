def next_greater_element(nums):

    stack = []    
    result = [-1] * len(nums)

    for i in range(2 * len(nums)):
        pos = i % len(nums)
        while len(stack) > 0 and nums[pos] > nums[stack[-1]]:
            j = stack.pop()
            result[j] = nums[pos]
        if i < len(nums):
            stack.append(i)
        print("i =", i, "stack =", stack)

    return result

tests = [
    ([1, 2, 1], [2, -1, 2]),
    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
    ([3, 3, 3], [-1, -1, -1]),
    ([5], [-1])
]

for nums, expected in tests:
    got = next_greater_element(nums)
    print("OK  " if got == expected else "FAIL", nums, "->", got, "expected")