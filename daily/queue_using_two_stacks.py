'''
Implement a queue class using two stacks.
A queue is a data structure that supports the FIFO protocol
(First in = first out).
Your class should support the enqueue and dequeue methods like a standard queue.
'''

class Queue:
  def __init__(self):
    self.__left = []
    self.__right = []
    
  def enqueue(self, val):
    if self.__left:
      self.__left.append(val)
    else:
      self.move_reverse(self.__right, self.__left)
      self.__left.append(val)
    print(self.__left)

  def dequeue(self):
    if self.__right:
      return self.__right.pop()
    else:
      self.move_reverse(self.__left, self.__right)
      return self.__right.pop()

  # move l1 to l2
  def move_reverse(self, l1, l2):
    len1 = len(l1)
    for _ in range(len1):
      l2.append(l1.pop())

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
# 1 2 3
