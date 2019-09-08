'''
From: Coding Interview Pro 31/08/2019
Problem: Find Pythagorean Triplets

Given a list of numbers, find if there exists a pythagorean triplet in that list.
A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
'''
import math

def findPythagoreanTriplets(nums):
  exists = {}
  for i in nums:
    exists[i] = True
  for a in nums:
    for b in nums:
      if a == b:
        continue
      c2 = pow(a, 2) + pow(b, 2) # c^2 = a^2 + b^2
      if exists.get(math.sqrt(c2), False):
        return True
  return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
print(findPythagoreanTriplets([5,2,3,4]))
# True
