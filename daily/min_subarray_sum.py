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
from collections import deque

class Solution:
  def minSubArrayLen(self, nums, s):
    if len(nums) == 0:
      return 0
    st = time.time()
    best = len(nums) + 1
    start = 0
    end = 0
    currsum = nums[0]  # represents sum of nums from indices start->end
    comps = 0
    if currsum >= s:
      return 1
    while start < len(nums):
      comps +=1
      if currsum >= s:
        newbest = end - start + 1
        if newbest < best:
          best = end - start + 1
        currsum -= nums[start]
        start += 1
      else:  # still less than s
        if end < len(nums) - 1:
          end += 1
          currsum += nums[end]
        if end + 1 == len(nums) and currsum < s:
          break
    print("optimised: %ss" % (time.time() - st), len(nums), comps)
    if best == len(nums) + 1:
      return 0
    else: 
      return best
        

      
      


    

  def bruteoptimised(self, nums, s):
    st = time.time()
    best = len(nums) + 1
    for pos in range(len(nums) + 1):  # list traversal
      if pos < len(nums) and nums[pos] >= s:
        return 1
      if best == len(nums) + 1:
        amount = nums[pos]
        for new_best in range(2, best-1):  # can be converted to log n by binary
          amount += nums[pos+new_best]
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
    print("brute optimised: %ss" % (time.time() - st))
    if best == len(nums) + 1:
      return 0
    else:
      return best


  def bruteforce(self, nums, s):
    st = time.time()
    comps = 0
    for size in range(len(nums) + 1):
      for i in range(len(nums) - size + 1):
        comps += 1
        amount = sum(nums[i:i+size])
        if amount >= s:
          print("brute: %ss" % (time.time() - st), len(nums), comps)
          return size
    print("brute: %ss" % (time.time() - st), len(nums), comps)
    return 0

# print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2



# tests:
arr = random.sample(range(20000), 20000)
num = 2000000
print(Solution().minSubArrayLen(arr, num))
print(Solution().bruteoptimised(arr, num))
print(Solution().bruteforce(arr, num))


# print(Solution().minSubArrayLen([1, 2, 3, 4, 5], 15))  # 5