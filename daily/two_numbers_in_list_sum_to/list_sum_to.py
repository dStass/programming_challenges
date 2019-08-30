'''
From: Daily Coding Problem 29/08/2019
Problem: 

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def does_sum(nums, k):
  prev = {}
  for num in nums:
    complement = k - num
    cexist = prev.get(complement, False)
    if cexist:
      return True
    else:
      prev[num] = True
  return False

print(does_sum([3,4,5,8,9],12))