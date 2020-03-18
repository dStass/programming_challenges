'''
Given a string of parentheses, find the balanced string that can be produced from it
using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example, given "(()",
you could return "(())". Given "))()(", you could return "()()()()".
'''

class Solution:
  def minAddToMakeValid(self, S: str) -> int:
    stack = []
    for s in S:
      if s == '(':
        stack.append(s)
        continue
      
      # case ')'
      if len(stack) == 0 or stack[-1] == ')':
        stack.append(s)
        continue
      
      # case ')' followed by '('
      stack.pop()
      
    return len(stack)

  def returnValid(self, S):
    stack = []
    require_closing = 0
    for s in S:
      if s == '(':
        stack.append(s)
        require_closing += 1
        continue
      
      # case ')'
      if len(stack) == 0 or stack[-1] == ')':
        stack.append('(')
        stack.append(s)
        continue
      
      require_closing -= 1
      stack.append(s)
    
    closing_suffix = ')' * require_closing



    return ''.join(stack) + closing_suffix



print(Solution().returnValid("(()))(("))