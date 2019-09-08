'''
From: Daily Interview Pro 24/08/2019
Problem: Two-Sum

You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.
'''

# AIM: in O(n) time
# for each ith item in list, check if k-i exists
def two_sum(list, k):
  if len(list) < 2:
    return False
  explored = {}
  for i in list:
    i_complement = k - i
    if (explored.get(i_complement, False)):
      return True
    else:
      explored[i] = True
  return False

print(two_sum([4,7,1,-3,2], 5))
# True
