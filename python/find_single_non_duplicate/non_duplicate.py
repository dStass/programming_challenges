'''
From: Daily Interview Pro 25/08/2019
Problem: Find the non-duplicate number

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
'''
import random

# O(N) solution, O(N) space complexity
# traverse and add to a dict if value hasn't already existed, else
# we pop the dict as we go as no values will appear more than once
# "traverse" the dict, we know there SHOULD only exist one missing number
# return it and we have found the number appearing only once
def singleNumber(nums):
  visited = {}
  for i in range(0, len(nums)):
    found = visited.pop(nums[i], False)
    if not found:
      visited[nums[i]] = True
  
  for key in visited:
    return key


# O(N^2 solution), O(1) space complexity
# first we sort the list using bubble sort (O(1) space complexity)
# Then we traverse the list and check values are paired up consecutively
# return when a pair cannot be found 
# Complexity: O(N^2) for bubble sort, O(N) to traverse list again
# O(N^2 + N + C) -> O(N^2) 
def singleNumberChallenge(nums):
  n = len(nums)  # one variable here denoting length of num list

  # bubble sort:
  for i in range(n):
    for j in range(n-i-1):
      if nums[j] > nums[j+1]:
        nums[j], nums[j+1] = nums[j+1], nums[j]  # swap
  
  # variable denoting the previous value
  prev = nums[0]
  for i in range(1, n-1):
    if i % 2 == 1:  # i is odd
      if nums[i] != prev:  # check if value is the same as prev
        return prev  # single value found, return it
    else:  # i is even (start of the next unique pair)
      prev = nums[i]
  return 0


# tests

N = 2500
generated = list(range(0,N))
generated.extend(list(range(0,N)))
random_index = random.randint(0,2*N)
del generated[random_index]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

print(random_index % N, singleNumber(generated))

print(random_index % N, singleNumberChallenge(generated))