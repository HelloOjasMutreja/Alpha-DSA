# Day 03: Recursion + bit intuition (Nov 03)

| # | Problem | Role | Approach | Time | Space | Edge case I missed |
|---|---------|------|----------|------|-------|--------------------|
| 1 | [Power of Two](power_of_two.py) | Primary | Reject n <= 0 and odd numbers above 1. Then test x = 0, 1, 2, ... and return True on n == 2**x, stopping when 2^x passes n. | O(log n) | O(1) | The odd check rejected 1, which is 2^0. Also n // 2**x == 1 isn’t an equality test: it matched 6 because 6 // 4 is 1. |
| 2 | [Power of Three](var_1_power_of_three.py) | Variant 1 | Very simply I changed the divisor from power of two to power of three in the recursion, then instead of filtering away the odd numbers previously, we filter away even numbers | O(log n) | O(1) | nothing really, this was quick |