'''
From Daily Interview Pro 29/08/2019
Problem: Maximum in the stack

Implement a class for a stack that supports all the regular functions (push, pop)
and an additional function of max() which returns the maximum element in the stack
(return None if the stack is empty).
Each method should run in constant time.
'''



# O(N) time complexity
class MaxStack:
  def __init__(self):
    self.max_stack_ = []
    self.stack_ = []

  def push(self, val):
    self.stack_.append(val)
    if len(self.max_stack_) == 0:
      self.max_stack_.append(val)
    else:
      last_max = self.max_stack_[len(self.max_stack_)-1]
      if val > last_max:
        self.max_stack_.append(val)
      else:
        self.max_stack_.append(last_max)

  def pop(self):
    if len(self.stack_) == 0:
      return None
    to_return = self.stack_[len(self.stack_)-1] 
    self.stack_ = self.stack_[:-1]
    self.max_stack_ = self.max_stack_[:-1]
    return to_return


  def max(self):
    length = len(self.max_stack_)
    if length == 0:
      return None
    return self.max_stack_[length-1]

  max_stack_ = []
  stack_ = []

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
