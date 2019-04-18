# Project Euler - Problem 1
# Zach Taylor

import math
import time

"""Calculate the sum of all natural numbers that are multiples of 
3 or 5 and less than 1000.

Details
-------
This algorithm uses the familiar sum formula
sum_{k=1}^n{k} = \frac{n*(n+1)}{2} (see pf. 1), noting that a number is
a multiple of both 3 and 5 if and only if it is a multiple of 15 (see pf. 2).

Proofs: 1, 2.

Complexity
----------
This algorithm is O(1) in both temporal and spatial complexity.
"""

print("Euler problem 1")
print("Calculating solution...")

start = time.time()
# Numbers that evenly divide the greatest multiple of 3, 5, and 15 
# less than 1000, respectively.
n, m, p = math.floor(1000/3), math.floor(1000/5), math.floor(1000/15)

# Use formula for sum, and subtract sum of multiples of 15, since those
# were counted twice
solution = int((3*n*(n+1) + 5*m*(m+1) - 15*p*(p+1))/2)
end = time.time()

print("Finished in {0:.7f} seconds".format(end - start))
print("Solution:", solution)