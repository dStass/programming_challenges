'''
From: Daily Interview Pro 03/09/2019
Problem: Longest Sequence with Two Unique Numbers

Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
'''

def findSequence(seq):
  visited = {}
  unique_count = 0
  substr = ""
  for i in range(len(seq)):
    found = visited.get(seq[i], 0)
    if found == 0:  # new num
      if unique_count == 2:

    

print findSequence([1, 3, 5, 3, 1, 3, 1, 5])
# 4
