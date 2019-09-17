'''
Problem: Intersection of Linked Lists
From: Coding Interview Pro 08/09/2019 (stub code)
      Daily Coding Problem 17/09/2019

You are given two singly linked lists.
The lists intersect at some node.
Find, and return the node.
Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4 

This should return 3
(you may assume that any nodes with the same value are the same node).
'''

# Assume lists WILL intersect
def intersection(a, b):
  n1 = a
  n2 = b
  check_first = True
  explored = {}
  while (True):
    n = n1 if check_first else n2
    val = n.val
    
    if explored.get(val, False):
      return n
    else:
      explored[val] = True

    if check_first:
      n1 = n1.next
      check_first = False
    else:
      n2 = n2.next
      check_first = True
    

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print(c.val, end=' ')
      c = c.next
    print()

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
