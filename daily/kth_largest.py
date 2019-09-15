'''
Problem: Kth largest element in a list
From: Coding Interview Pro 15/09/2019

Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
'''
def findKthLargest(nums, k):
  nums = list(dict.fromkeys(nums))  # remove dups
  if k > len(nums):
    return None
  nums.sort()  # sort
  return nums[len(nums) - k]  # kth from end

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

# Tests
print(findKthLargest([3, 5, 2, 4, 6, 8], 6))  # 2
print(findKthLargest([3, 5, 2, 4, 6, 8], 7))  # None
print(findKthLargest([1,1,1,1,1], 2))  # None
print(findKthLargest([1,2,3,3,4], 3))  # 2
print(findKthLargest([], 1))

