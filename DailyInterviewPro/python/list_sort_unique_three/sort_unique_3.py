'''
From: Daily Interview Pro 23/08/2019
Problem: Sorting a list with 3 unique numbers

Given a list of numbers with only 3 unique numbers (1, 2, 3),
sort the list in O(n) time.
'''

def sortNums(nums):
  to_return = []
  freq = {1:0, 2:0, 3:0}
  for num in nums:  # N items in list
    freq[num] += 1
  for key in freq:  # for each key (ie 1,2,3 in this case)
    to_return.extend([key]*freq[key])  # [2]*4 = [2,2,2,2]
  return to_return

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
