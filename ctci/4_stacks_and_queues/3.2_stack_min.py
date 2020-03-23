# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class StackMin:
  stack = None
  def __init__(self):
    self.stack = []

  def push(self, val):
    # append val:
    self.stack.append(val)

    # insert min at start of stack
    self.stack.insert(0, min(self.stack[0], val))
  
  def pop(self):
    if len(self.stack) == 0:
      return 'ERROR: EMPTY STACK'
    
    to_return = self.stack.pop()
    self.stack.pop(0)

  def min(self):
    if len(self.stack) == 0:
      return 'ERROR: EMPTY STACK'
    return self.stack[0]
  
  def print(self):
    print(self.stack)

stack = StackMin()
stack.push(8)
stack.push(2)
stack.push(5)
stack.push(17)

stack.print()

stack.print()
print("MIN = ", stack.min())
print("poppping =", stack.pop())
stack.print()
print("MIN = ", stack.min())
print("poppping =", stack.pop())
stack.print()
print("MIN = ", stack.min())
print("poppping =", stack.pop())
stack.print()
print("MIN = ", stack.min())
