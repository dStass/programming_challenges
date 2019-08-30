'''
From: Daily Interview Pro 30/08/2019
Problem: Number of ways to climb stairs

You are given a positive integer N which represents the number of steps in a staircase.
You can either climb 1 or 2 steps at a time.
Write a function that returns the number of unique ways to climb the stairs.
'''

import math
from decimal import Decimal


# O(1)
# Solve recurrence relation a_n = a_n-1 + a_n-2
# char eqn: r2 - r - 1 = 0
# r1,2 = (1 +- sqrt(5))/2
# solve fn = a*r1^n + b*r2^n
# f(0) = a + b = 1 (ways to get to step 0 = 1)
# f(1) = a * r1 + b * r2 = 1
# . . . fn = 1/sqrt(5) * [(1+sqrt(5))/2]^(n+1) - 1/sqrt(5) * [(1-sqrt(5))/2]^(n+1)
def staircase_eval(n):
  phip = Decimal((1+math.sqrt(5))/2)
  phin = Decimal((1-math.sqrt(5))/2)
  a = Decimal(1/math.sqrt(5))
  b = Decimal(-1/math.sqrt(5))
  fibn = a * phip**(n+1) + b * phin**(n+1)
  return int(str(fibn))


# fibonacci sequence
# DP: O(N) time, O(1) space
def staircase(n):
  prev = 1
  curr = 1
  for i in range(2, n+1):
    temp = curr
    curr += prev
    prev = temp
  return curr
  

N = 800
print(staircase_eval(N))
print(staircase(N))