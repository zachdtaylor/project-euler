# Project Euler - Problem 1
# Zach Taylor

import math
import time

"""Calculate the sum of all natural numbers that are multiples of
3 or 5 and less than 1000.

Details
-------
This algorithm uses the familiar sum formula
sum_{k=1}^n{k} = \frac{n*(n+1)}{2} (see thm. 1), noting that a number is
a multiple of both 3 and 5 if and only if it is a multiple of 15 (see thm. 2).

Theorems: 1, 2.

Complexity
----------
This algorithm is O(1) in both temporal and spatial complexity.
"""

print("Euler problem 1")
n = int(input("n="))
print("Calculating solution...")

start = time.time()
max_lt_n = n-1
# Numbers that evenly divide the greatest multiple of 3, 5, and 15
# less than 1000, respectively.
a, b, c = math.floor(max_lt_n/3), math.floor(max_lt_n/5), math.floor(max_lt_n/15)
# Use formula for sum, and subtract sum of multiples of 15, since those
# were counted twice
solution = int((3*a*(a+1) + 5*b*(b+1) - 15*c*(c+1))/2)
end = time.time()

print("Finished in {0:.7f} seconds".format(end - start))
print("Solution:", solution)
