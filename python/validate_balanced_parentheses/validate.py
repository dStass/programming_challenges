'''
From: Daily Interview Pro 20/08/2019
Problem: Validate Balanced Parentheses

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
'''

pairs = {'(': ')', '[': ']', '{': '}'} # each open char keys to a close

class Solution:
  def isValid(self, s):
    stack = [] # list
    for c in s:
      # if c is an opening char, add it to stack
      if c in pairs:
        stack += c
      else: # if c is a closing char
        if c == pairs.get(stack[-1]): # check if it matches last thing in the stack
          stack = stack[:-1]
        else:
          return False

    if len(stack) != 0: # check size is 0
      return False

    return True

    # Fill this in.

# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "()(){(())}{{}()([(]})"
# should return False
print(Solution().isValid(s))
