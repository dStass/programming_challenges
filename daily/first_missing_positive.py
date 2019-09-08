'''
From: Online Coding Problem 01/09/2019
Problem: First missing positive integer

Given an array of integers, find the first missing positive
integer in linear time and constant space - O(N) time and O(1) space
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def get_first_missing_pos(nums):
  # first we move positive numbers to the front
  # and negative to back of list
  # segregate returns index of the final positive number before negatives
  endex = segregate(nums)
  
  # traverse new nums list, get value and assign the INDEX
  # of that value to negative, we associate existence 
  # as a negative value
  for i in range(endex + 1):
    if abs(nums[i] - 1) > endex:
      continue
    nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
  
  # return first non-negative INDEX
  # it is non-negative since number did NOT exist
  # in array to make it negative in the first place
  for i in range(endex + 1):
    if nums[i] > 0:
      return i + 1

  return endex + 1


# moves negative numbers to the end
# we only check n items
def segregate(nums):
  endex = len(nums) - 1
  i = 0
  while i < endex:
    while nums[i] <= 0:
      temp = nums[endex]
      nums[endex] = nums[i]
      nums[i] = temp
      endex -= 1
    i += 1
  return endex # last positive integer loc


print(get_first_missing_pos([3,4,-1,1]))
print(get_first_missing_pos([1,2,0]))
