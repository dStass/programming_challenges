'''
Given an array of characters with repeats, compress it in place.
The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
'''

class Solution(object):
  def compress(self, chars):
    if len(chars) < 2:
      return chars
    to_return = []
    prev_char = chars[0]
    to_return.append(prev_char)
    for i in range(1, len(chars)):
      if chars[i] == prev_char:
        count = None
        try:
          count = int(to_return[-1])
        except ValueError:
          count = None
        if count:
          to_return[-1] = str(count+1)
        else:
          to_return.append(str(2))
      else:
        to_return.append(chars[i])
        prev_char = chars[i]
    
    return to_return
      

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']
