'''
Problem: Min Range Needed to Sort 22/10/2019

Given a list of integers, return the bounds of the minimum range
that must be sorted so that the whole list would be sorted.

Example:
Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)

Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.
'''

def findRange(nums):
  if len(nums) < 1:
    return None

  snums = sorted(nums)
  start = -1
  end = -1
  for i in range(len(nums)):
    if snums[i] != nums[i]:
      start = i
      break
  for i in range(len(nums) - 1, -1, -1):
    if snums[i] != nums[i]:
      end = i
      break
  if start == -1:
    return None
  return [start, end]

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
print(findRange([1, 2])) # None - list already sorted
print(findRange([3, 2])) # 0 -> 1
