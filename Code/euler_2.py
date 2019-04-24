# Project Euler - Problem 2
# Zach Taylor

import math
import time
import sys

"""Calculate the sum of all even Fibonacci numbers less than n = 4 million.

Details
-------
This algorithm uses the fact that the even Fibonacci numbers follow the
recurrence relation E_n = 4E_{n-1} + E_{n-2} (see thm. 5) combined with
dynamic programming to reduce the spacial complexity.

Theorems: 3, 4, 5

Complexity
----------
Temporal: O(log(n))
Spacial: O(1)
"""

print("Euler problem 2")
print("Calculating solution...")

start = time.time()
E_1, E_2, E_3 = 2, 8, 34
solution = E_1 + E_2
while E_3 < 4000000:
  solution += E_3
  E_1 = E_2
  E_2 = E_3
  E_3 = 4*E_2 + E_1
  iters += 1
end = time.time()

print("Finished in {0:.7f} seconds".format(end - start))
print("Solution:", solution)
