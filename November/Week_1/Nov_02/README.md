# Day 02: Recursion → bottom-up DP (Nov 02)

| # | Problem | Role | Approach | Time | Space | Edge case I missed |
|---|---------|------|----------|------|-------|--------------------|
| 1 | [Climbing Stairs](climbing_stairs.py) | Primary | for each count x of 2-steps, there are n - x moves in total, and we choose which x slots are the 2-steps. Add C(n - x, x) over all x from 0 to n // 2. C is computed with a hand-written factorial. | O(n^2) | O(n) | the loop stopped one short because range(n // 2) excludes its end value. That made n = 1 return 0 and every other answer too small. |

