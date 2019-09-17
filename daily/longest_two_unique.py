'''
Problem: Longest Sequence with Two Unique Numbers
From: Coding Interview Pro 03/09/2019

Given a sequence of numbers, find the longest sequence
that contains only 2 unique numbers.

Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4

The longest sequence that contains
just 2 unique numbers is [3, 1, 3, 1]
'''
from numpy.random import seed
from numpy.random import randint

# Moving window with indices: start -> end
# loop while 
def findSequence(seq):
  if len(seq) < 2:
    return None
  comps = 0
  start = 0
  end = 0
  curr_table = {}
  best = 0
  curr_table[seq[0]] = 1
  while end < len(seq) - 1:
    comps += 1
    if len(curr_table) <= 2:
      end += 1
      val = curr_table.get(seq[end], 0) + 1
      curr_table[seq[end]] = val
      if len(curr_table) <= 2:
        best = max(end-start+1, best)
    else:
      val = curr_table.get(seq[start])
      if val:
        if val > 1:
          curr_table[seq[start]] = val - 1
        else:
          del curr_table[seq[start]]
      start += 1
  print("comps ratio", comps, float(comps) / float(len(seq)))
  return best


arr = randint(0, 10, 2000000)

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
print(findSequence([1, 3, 5, 3, 1, 4, 1, 5]))
print(findSequence(arr))
# 4
