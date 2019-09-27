'''
Problem: Trapping Rainwater
From: Coding Interview Pro 24/09/2019

You have a landscape, in which puddles can form.
You are given an array of non-negative integers representing the
elevation at each location. Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because
6 units of water can get trapped here.

          X               
      X███XX█X              
    X█XX█XXXXXX                   
#  010210132121

leetcode: HARD Problem
Solution submission faster than ~98% of other submissions
'''
from collections import deque

def capacity(arr):

  # need at least 3 elevations to trap water
  if len(arr) < 3:
    return 0

  # deque contains maximas in form:
  # list : [index, elevation at index] 
  maximas = deque()
  
  highest = arr[0]

  # Gather local maximas
  # a value larger than the one to its left
  # and greater than or equal to the one on its right
  if arr[0] >= arr[1]:
    maximas.append([0, arr[0]])

  for i in range(1, len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] >= arr[i+1]:
      maximas.append([i, arr[i]])
    if arr[i] > highest:
      highest = arr[i]
  
  last = len(arr) - 1
  if arr[last] > arr[last - 1]:
    maximas.append([last, arr[last]])
    if arr[i] > highest:
      highest = arr[i]


  if len(maximas) < 2:
    return 0

  # gotten all maximas
  # now we make it so maximas are increasing left of the highest
  # elevation and decreasing right of highest
  # eg elevation: remove 2 and work out how much water
  # gets retained beween 4 and 0
  #          # #
  #  #       # # #   #
  #  #   #   # # # # #
  #  # # # # # # # # # #
  #  0 1 2 3 4 5 6 7 8


  highest_reached = False
  max_revised = []  # use a stack
  max_revised.append(maximas[0])
  i = 1
  while i < len(maximas):
    curr = maximas[i]
    curr_height = curr[1]
    prev_height = max_revised[-1][1]
    
    if curr_height == highest:
      highest_reached = True

    if not highest_reached and curr_height >= prev_height:
      max_revised.append(curr)

    # add all remaining highests
    if highest_reached and curr_height == highest:
      max_revised.append(curr)
    i += 1

  # go the opposite way
  # from right to left increasing
  # stop when we get to an elevation of the highest
  i = len(maximas) - 1
  max_revised_reverse = [] # opposite way
  max_revised_reverse.append(maximas[i])
  i -= 1

  while i >= 0:
    curr = maximas[i]
    curr_height = curr[1]
    prev_height = max_revised_reverse[0][1]

    if curr[1] == highest:
      break

    if curr_height > prev_height:
      max_revised_reverse.insert(0,curr)
    i -= 1

  max_revised += max_revised_reverse
  
  total_retention = 0
  for mi in range(1, len(max_revised)):
    m_curr = max_revised[mi]
    m_prev = max_revised[mi-1]

    # choose min 
    max_retention = min(m_curr[1], m_prev[1])
    retention = 0
    for i in range(m_curr[0] - 1, m_prev[0], -1):

      # add if less than or equal to max retention of water 
      # we can hold
      if arr[i] <= max_retention:
        retention += (max_retention - arr[i])

    # add to total
    total_retention += retention
  return total_retention


# #         X               
# #     X███XX█X              
# #   X█XX█XXXXX                  
# #  01021013212

# print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2]))
# # 6

# #          X
# #         XX█X              
# #     X███XXXX█X              
# #   X█XX█XXXXXXXX                   
# #  01021013433121

# print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 4, 2, 3, 1, 2, 1]))
# # 7

# print(capacity([1,2,1]))
# # 7


# Tests
cap = [1,0]
print(capacity(cap) == 0)

cap = [1,1,1]
print(capacity(cap) == 0)

cap = [1,0,1]
print(capacity(cap) == 1)

cap = [1,2,1]
print(capacity(cap) == 0)

cap = [1,0,5]
print(capacity(cap) == 1)

cap = [5,0,5]
print(capacity(cap) == 5)

cap = [5,0,6,1,5]
print(capacity(cap) == 9)

cap = [5,2,0,2,5]
print(capacity(cap) == 11)  # 3+5+3

cap = [5,0,6,1,6]
print(capacity(cap) == 10)

cap = [5,0,6,1,7,7,7,6,7,7]
print(capacity(cap) == 11)  # 5+5+1

cap = [5,0,6,1,7,7,7,9,0,2,0,5]
print(capacity(cap) == 23)  # 5+5+0..0+5+3+5

cap = [2,8,5,5,6,1,7,4,5]
print(capacity(cap) == 12)