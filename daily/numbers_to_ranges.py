'''
Problem: Merge List of Numbers Into Ranges
From: Coding Interview Pro 14/10/2019

Given a sorted list of numbers,
return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']

Assume that all numbers will be greater than or equal to 0,
and each element can repeat.

'''

def findRanges(nums):
  if len(nums) == 0:
    return []

  to_return = []
  range_start = nums[0]
  prev = nums[0]
  for i in range(1, len(nums)):
    if nums[i] == prev or nums[i] == prev + 1:
      prev = nums[i]
      continue

    range_str = get_range(range_start, prev)
    to_return.append(range_str)
    range_start = nums[i]
    prev = nums[i]
  
  range_str = get_range(range_start, prev)
  to_return.append(range_str)

  return to_return

def get_range(start, end):
  range = str(start)
  range += "->"
  range += str(end)
  return range

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15,16]))
# ['0->2', '5->5', '7->11', '15->16']

print(findRanges([0]))
# ['0->0']

print(findRanges([0,0,0,0,0]))
# ['0->0']

print(findRanges([0,0,0,0,0,1,1,1,2]))
# ['0->2']

print(findRanges([-2,0,0,0,0,0,1,1,1,2,5]))
# ['-2->-2', '0->2', '5->5']

print(findRanges([0, 2, 4]))
# ['0->0', '2->2', '4->4']
