'''
Problem: Largest Product of 3 Elements
From: Coding Interview Pro 17/09/2019

You are given an array of integers.
Return the largest product that can be made by multiplying
any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by
multiplying -4 * -4 * 8 = 128.
'''

def maximum_product_of_three(lst):
  if len(lst) < 3:
    return None

  # max of product(top three)
  # OR largest element product(largest, 2 smallest) for negative cases
  lst.sort() # first sort list
  end = len(lst) - 1
  first = 0
  return max( (lst[end] * lst[end - 1] * lst[end - 2]), 
              (lst[end] * lst[first] * lst[first + 1]))

  


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
