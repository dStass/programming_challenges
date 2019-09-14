'''
Problem: Move Zeros
From: Coding Interview Pro 14/09/2019

Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order of
the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
  def moveZeros(self, nums):
    swap_index = -1
    for i in range(len(nums)):
      if nums[i] == 0 and swap_index == -1:
        swap_index = i
      if nums[i] != 0 and swap_index >= 0:
        nums[swap_index] = nums[i]
        nums[i] = 0
        swap_index += 1


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

# tests:
nums = [2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0]

nums = [2, 0, 1, 3, 4]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0]

nums = [0]
Solution().moveZeros(nums)
print(nums)
# [0]

nums = [0, 0]
Solution().moveZeros(nums)
print(nums)
# [0, 0]

nums = [1, 1]
Solution().moveZeros(nums)
print(nums)
# [1, 1]


