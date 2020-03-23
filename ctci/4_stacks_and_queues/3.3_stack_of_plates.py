'''
Stack of Plates:

Imagine a (literal) stack of plates. If the stack gets too high, it might topple.

Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold.

Implement a data structure SetOfStacks that mimics this.

SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity.

SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack. 
'''

class SetOfStacks:
  stacks = None
  STACK_LEN = None

  def __init__(self, val = 5):
    self.stacks = [[]]
    self.STACK_LEN = val
  
  def push(self, val):
    last_stack = self.stacks[-1]
    if len(last_stack) == self.STACK_LEN:
      new_stack = [val]
      self.stacks.append(new_stack)
    else:
      last_stack.append(val)
      self.stacks[-1] = last_stack
  
  def pop(self):
    if len(self.stacks) == 1 and len(self.stacks[0]) == 0:
      return 'ERROR: EMPTY STACK'
    
    # get the last stack we are popping from
    last_stack = self.stacks[-1]
    if len(last_stack) == 0:
      self.stacks.pop()

    last_stack = self.stacks[-1]
    to_return = last_stack.pop()
    return to_return

  def popAt(self, val):
    if val >= len(self.stacks) or val < 0:
      return 'ERROR: SUB-STACK NOT FOUND'
    
    if len(self.stacks[val]) == 0:
      return 'ERROR: SUB-STACK NOT FOUND'
    
    to_return = self.stacks[val].pop()  # pop end value of val stack
    while val < len(self.stacks):
      next_val = val + 1
      if next_val < len(self.stacks):  # ie there is a next list
        if len(self.stacks[next_val]) == 0:
          self.stacks.pop()
        else:
          self.stacks[val].append(self.stacks[next_val].pop(0))
      val = next_val
    return to_return


    # some cases:
    # either len stacks[val] == 1, then we just pop
    # or len stacks[val] == 5 and 
    
    

  def print(self):
    print(self.stacks)


stacks = SetOfStacks()
for i in range(11):
  stacks.push(i)
stacks.print()
stacks.popAt(0)
stacks.print()

stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.popAt(0)
stacks.print()
# stacks.print()
# stacks.pop()
# stacks.pop()
# stacks.pop()
# stacks.pop()
# stacks.pop()
# print(stacks.pop())
# stacks.print()
# print(stacks.pop())
# stacks.print()


