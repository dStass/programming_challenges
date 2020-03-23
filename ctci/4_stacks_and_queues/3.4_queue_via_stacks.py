'''
Queue via Stacks:

Implement a MyQueue class which implements a queue using two stacks
'''


class MyQueue:
  stack_push = None
  stack_pop = None
  
  def __init__(self):
    self.stack_push = []
    self.stack_pop = []

  def push(self, value):

    # transfer from stack_pop to stack_push before we push to stack
    if len(self.stack_push) == 0:
      for _ in range(len(self.stack_pop)):
        self.stack_push.append(self.stack_pop.pop())

    self.stack_push.append(value)

  def pop(self):
    if len(self.stack_push) == 0 and len(self.stack_pop) == 0:
      return 'EMPTY QUEUE'
    
    if len(self.stack_pop) == 0:
      for _ in range(len(self.stack_push)):
        self.stack_pop.append(self.stack_push.pop())
    
    return self.stack_pop.pop()

  def print(self):
    if len(self.stack_push) == 0:
      print(self.stack_pop)
    
    else:
      print(self.stack_push[::-1])


q = MyQueue()
print(q.pop())

q.push(1)
q.push(2)
q.push(3)
q.print()
print("POPPING ", q.pop())
q.print()
q.push(4)
q.print()
print("POPPING ", q.pop())
q.print()

