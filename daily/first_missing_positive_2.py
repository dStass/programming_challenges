'''
Problem: First missing positive integer
From: Coding Interview Pro 28/09/2019

You are given an array of integers.
Return the smallest positive integer that is not present in the array.
The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because
it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
'''

def first_missing_positive(nums):
  if len(nums) == 0:
    return 1
  
  if len(nums) == 1:
    if nums[0] != 1:
      return 1
    else:
      return 2
      

  # swap index starts from end of array
  # move this swap index left until no longer neg
  swap_index = len(nums) - 1
  while nums[swap_index] <= 0:
    if swap_index == 0:
      return 1
    swap_index -= 1

  # split array
  i = 0
  while i <= swap_index:
    if nums[i] <= 0:
      temp = nums[i]
      nums[i] = nums[swap_index]
      nums[swap_index] = temp
      while nums[swap_index] <= 0:
        if swap_index == 0:
          return 1
        swap_index -= 1
    i+=1
  
  print(nums, swap_index)
  
  i = 0
  while i <= swap_index:
    if abs(nums[i]) <= len(nums) and nums[abs(nums[i])-1] >= 0:
      nums[abs(nums[i])-1] = - nums[abs(nums[i])-1]
    i += 1

  print(nums, swap_index)
  i = 0
  while i <= swap_index:
    if nums[i] > 0:
      return i+1
    i+=1
  return i+1



print(first_missing_positive([-1, 3, 2, 4, 1, -5,20,-5,13]))
# 2

print(first_missing_positive([1, 2 , 0]))

print(first_missing_positive([-1,-2]))