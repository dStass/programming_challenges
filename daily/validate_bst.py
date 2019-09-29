'''
Problem: Validate Binary Search Trees
From: Coding Interview Pro 29/09/2019

You are given the root of a binary search tree.R
eturn true if it is a valid binary search tree, and false otherwise.
Recall that a binary search tree has the property that all values in the
left subtree are less than or equal to the root, and all values in the right subtree
are greater than or equal to the root.
'''

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  true_so_far = True
  if root.left:
    if root.left.key >= root.key:
      true_so_far = False
    else:
      true_so_far = is_bst(root.left)
  if root.right:
    if root.right.key <= root.key:
      true_so_far = False
    else:
      if true_so_far:
        true_so_far = is_bst(root.right)
  return true_so_far
  



a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a) == True)

#    5
#   / \
#  3   7
# / \ /
#1  4 6
# TRUE

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(8)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a) == False)

#    5
#   / \
#  3   7
# / \ /
#8  4 6
# FALSE

a = TreeNode(5)
print(is_bst(a) == True)  # True

a.right = TreeNode(1)
print(is_bst(a) == False)  # False