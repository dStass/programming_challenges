'''
Problem: Reverse Integer 23/10/2019

Write a function that reverses the digits a 32-bit signed integer, x.
Assume that the environment can only store integers
within the 32-bit signed integer range, [-2^31, 2^31 - 1].
The function returns 0 when the reversed integer overflows. 

Example:
Input: 123
Output: 321
'''

class Solution:
  OVERFLOW_LIMIT = 2**31
  def reverse(self, x):
    if x >= self.OVERFLOW_LIMIT or x <= -self.OVERFLOW_LIMIT:
      return 0
    else:
      x_str = str(x)
      x_str_reverse = x_str[::-1]
      return int(x_str_reverse)

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
print(Solution().reverse(2**32))