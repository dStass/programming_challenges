#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
  # all possible 3x3 magic square configurations
  possible = [[8, 1, 6, 3, 5, 7, 4, 9, 2], 
              [6, 1, 8, 7, 5, 3, 2, 9, 4],
              [4, 3, 8, 9, 5, 1, 2, 7, 6],
              [2, 7, 6, 9, 5, 1, 4, 3, 8],
              [2, 9, 4, 7, 5, 3, 6, 1, 8],
              [4, 9, 2, 3, 5, 7, 8, 1, 6],
              [6, 7, 2, 1, 5, 9, 8, 3, 4],
              [8, 3, 4, 1, 5, 9, 6, 7, 2]]

  sq = []
  for i in s:
      sq.extend(i)

  min = 9*9 # val = 9 x 9 positions

  for p in possible:

    cost = difference(p, sq)
    if cost < min:
      min = cost

  return min 



def difference(p, s):
  total = 0
  for i in range(len(p)):
    total += abs(p[i] - s[i])
  return total


s = []
s.append([4,8,2])
s.append([4,5,7])
s.append([6,1,6])

result = formingMagicSquare(s)
print("result=", result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = []

#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))

#     result = formingMagicSquare(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
