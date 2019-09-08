class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    to_return = ''
    for row in range(numRows):
      pos = row
      first = True
      last_change = 1
      while pos < len(s):
        to_return += s[pos] if last_change != 0 else ''
        if first:
          first = False
        else:
          first = True
        if not first:
          last_change = (numRows - 1 - row)*2
          pos += last_change
        else:
          last_change =  2*row
          pos += last_change
    return to_return
            

string = "abc"
print("result=", Solution().convert(string, 1))