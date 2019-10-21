'''
Problem: Arithmetic Binary Tree
From: Daily Interview Pro 19/10/2019

You are given a binary tree representation of an arithmetic expression.
In this tree, each leaf is an integer value
and a non-leaf node is one of the four operations:
'+'
'-'
'*'
'/'

Write a function that takes this tree and evaluates the expression.

Example:
    *
   / \
  +    +
 / \  / \
3  2  4  5
'''
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"
UNDEF = "UNDEF"

def evaluate(root):
  if root == None:
    return
  left = evaluate(root.left)
  right = evaluate(root.right)
  if left == UNDEF or right == UNDEF:
    return UNDEF

  if root.val == PLUS:
    return left + right
  elif root.val == MINUS:
    return left - right
  elif root.val == TIMES:
    return left * right
  elif root.val == DIVIDE:
    if right == 0:
      return UNDEF
    return left / right
  else:
    return root.val

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45

tree = Node(DIVIDE)
tree.left = Node(5)
tree.right = Node(DIVIDE)
tree.right.left = Node(DIVIDE)
tree.right.left.left = Node(5)
tree.right.left.right = Node(0)
tree.right.right = Node(1)
print(evaluate(tree))
# 5/((5/0)/1) ===> UNDEFINED