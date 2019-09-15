'''
Problem: Largest sum of non-adjacent numbers
From: Daily Coding Problem 06/09/2019 [HARD]

Given a list of integers, write a function that returns
the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example,
[2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10 since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

# Solved with DP
# traverse from left to right, 
# for each index, set it to the largest between:
#   - itself
#   - 1 hop
#   - 2 hops
#   - itself + 1 hop (closest non-adjacent), eg [1,2,3] 3 and 1
#   - itself + 2 hops (not considered when i == 2)  eg [1,2,3,4] 4 and 2 OR 4 and 1
# (a hop represents how many adjacent numbers AREN't included)
# - we do not need to consider 3 hops as this would have
# been covered by the 1 hop case
def max_nonad(nums):
  if len(nums) == 0:
    return None
  if len(nums) == 1:
    return nums[0]

  for i in range(2, len(nums)):
    if i == 2:
      nums[i] = max(nums[i],
                    nums[i] + nums[i-2],
                    nums[i-2])
    else:
      nums[i] = max(nums[i], 
                    nums[i-2], 
                    nums[i-3],
                    nums[i] + nums[i-2],
                    nums[i] + nums[i-3])
    print(nums)
  return max(nums[len(nums) - 1], nums[len(nums) - 2])

nums = [2, 4, 6, 2 , 5]
print(max_nonad(nums))  # 13

nums = [5,1,1,5]
print(max_nonad(nums))   # 10

nums = [5, 5, 10, 100, 10, 5]
print(max_nonad(nums))  # 110

nums = [-3, -5, -8, -1, -2]
print(max_nonad(nums))  # -1

nums = [-3, -5, -8, -1, 90]
print(max_nonad(nums))  # 90

nums = [-1, -1, 1, -5, -8, -1, 90]
print(max_nonad(nums))  # 91

