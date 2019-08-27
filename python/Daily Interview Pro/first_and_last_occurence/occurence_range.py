'''
From: Daily Interview Pro 21/08/2019
Problem: First and Last Indices of an Element in a Sorted Array

Given a sorted array, A, with possibly duplicated elements, find the indices of the first
and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''

class Solution: 
  def getRange(self, arr, target):
    size = len(arr)
    first = -1
    last = -1
    for i in range(size):
      if arr[i] == target:
        last = i
        if first == -1:
          first = i
    return [first, last]


# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]


arr2 = [1,3,3,5,7,8,9,9,9,15]
x2 = 9
print(Solution().getRange(arr2, x2))

arr3 = [100, 150, 150, 153]
x3 = 150
print(Solution().getRange(arr3, x3))

arr4 = [1,2,3,4,5,6,10]
x4 = 9
print(Solution().getRange(arr4, x4))