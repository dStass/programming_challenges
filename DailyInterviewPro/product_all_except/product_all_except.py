'''
From: Daily Coding Problem 30/08/2019
Problem: Product of all elements except at position

Given an array of integers, return a new array
such that each element at index i of the new array
is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

# no division - in O(2n) --> O(n)
def get_sums_challenge(nums):
  to_return = [1] * len(nums)
  max = 1
  for i in range(len(nums)):
    to_return[i] *= max
    max *= nums[i]

  max = 1
  for i in range(len(nums)-1, -1, -1):
    to_return[i] *= max
    max *= nums[i]
  
  return to_return



def get_sums(nums):
  to_return = [0] * len(nums)
  max = 1
  for i in nums:
    max*=i
  for i in range(len(nums)):
    to_return[i] = int(max/nums[i])
  return to_return

print(get_sums_challenge([1,2,3,4,5]))