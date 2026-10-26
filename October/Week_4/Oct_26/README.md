# Day 26: Monotonic Stack (Oct 26)

| # | Problem | Role | Approach | Time | Space | Edge case I missed |
|---|---------|------|----------|------|-------|--------------------|
| 1 | [Next Greater Element I](next_greater_element.py) | Primary | We take a stack to be able to compare the latest numbers with the next number and then compare if the next element is greater, then when we do find the greater number, we pop the stack and add the key and value to the dictionary which we will use later when checking with the other array and ultimately printing results | O(n) | O(n) | I checked for top of the stack with stack[-1] while stack was empty [] |


![alt text](image.png)