'''
Problem: Minimum Size Subarray Sum
From: Coding Interview Pro 06/09/2019

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum >= s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: the subarray [4,3] has the minimal length
under the problem constraint.
'''
import random
import time

class Solution:
  def minSubArrayLen(self, nums, s):
    st = time.time()
    best = len(nums) + 1
    for pos in range(len(nums) + 1):  # list traversal
      # print("best=", best)
      if pos < len(nums) and nums[pos] >= s:
        return 1
      
      if best == len(nums) + 1:
        for new_best in range(2, best):  # can be converted to log n by binary
          amount = sum(nums[pos:pos+new_best])
          if amount >= s and new_best <= best:
            best = new_best
            break
      else:  # found
        for new_best in range(best-1, 1, -1):
          amount = sum(nums[pos:pos+new_best])
          if amount >= s and new_best <= best:
            best = new_best
            break
          if amount < s:
            break


    print("optimised: %ss" % (time.time() - st))
    if best == len(nums) + 1:
      return 0
    else:
      return best

  def bruteforce(self, nums, s):
    st = time.time()
    for size in range(len(nums) + 1):
      for i in range(len(nums) - size + 1):
        amount = sum(nums[i:i+size])
        if amount >= s:
          print("brute: %ss" % (time.time() - st))
          return size
    print("brute: %ss" % (time.time() - st))
    return 0

# print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2



# tests:
arr = random.sample(range(10000), 10000)
num = 2000000
print(Solution().minSubArrayLen(arr, num))
print(Solution().bruteforce(arr, num))


# print(Solution().minSubArrayLen([1, 2, 3, 4, 5], 15))  # 5