'''
Problem: Jump to the End
From: Daily Interview Pro 28/10/2019

Starting at index 0, for an element n at index i,
you are allowed to jump at most n indexes ahead.
Given a list of numbers,
find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2: 
3 -> 5 -> 4
'''

def jumpToEnd(nums):
  if len(nums) == 0:
    return -1
  if nums[0] == 0:
    if len(nums) == 1:
      return 0
    else:
      return -1
  
  # first we for each element - how it can be reached with 1 jump
  # ie for each index i containing element e,
  # for the next e indices from i, add i as an incoming point
  # add into a set so we don't duplicate
  
  can_be_reached_by_index = [set() for _ in range(len(nums))]
  for i in range(len(can_be_reached_by_index)):
    num_jumps = nums[i]
    for j in range(1, num_jumps+1):
      jump_to_index = i+j
      if jump_to_index < len(nums):
        can_be_reached_by_index[jump_to_index].add(i)


  # solution using DP 
  # first we make a list jumps required to get to each index at nums
  # check for each of the incoming indices from above:
  # the min jump at those indices and pick the minimum
  # to set as its jump amount
  # we also add 1 to signify a jump
  jumps = [0] * len(nums)
  for i in range(1, len(jumps)):
    least_amount = -1
    for jump_from in can_be_reached_by_index[i]:
      amount = jumps[jump_from]
      if least_amount == -1:
        least_amount = amount
      else:
        if amount < least_amount:
          least_amount = amount
    jumps[i] = least_amount + 1

  # to get to the end, we pick the end value
  return jumps[-1]


print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
print(jumpToEnd([3]))
print(jumpToEnd([0]))
print(jumpToEnd([0, 4])) # unable to reach end if first index is 0
print(jumpToEnd([1,1,1,1,1,1])) # will require 5 jumps to reach end
print(jumpToEnd([2,2,2,1,1,1])) # will require 3 jumps to reach end (2,2,1)
print(jumpToEnd([2,2,2,2,1,1])) # will require 3 jumps to reach end (2,2,1)
print(jumpToEnd([2,2,3,99,99,99])) # will require 2 jumps to reach end (2,3)
# 2
