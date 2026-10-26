def next_greater_element(nums1, nums2):

    stack = []
    next_greater = {}

    for i in range(len(nums2)):
        while len(stack) > 0 and nums2[i] > stack[-1]:
            next_greater[stack[-1]] = nums2[i]
            stack.pop()    
        stack.append(nums2[i])
        print("i =", i, "stack =", stack, "dict =", next_greater)
    
    result = []

    for i in range(len(nums1)):
        if nums1[i] in next_greater:
            result.append(next_greater[nums1[i]])
        else:
            result.append(-1)

    return result

tests = [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 5, 1], [5, 2, 6, 1, 7], [6, 6, 7]),
    ([3, 4, 8], [2, 7, 3, 5, 4, 6, 8], [5, 6, -1]),
]

for nums1, nums2, expected in tests:
    got = next_greater_element(nums1, nums2)
    print("OK  " if got == expected else "FAIL", nums1, nums2, "->", got, "expected")