'''
Problem: Create a balanced binary search tree
From: Coding Interview Pro 23/09/2019

Given a sorted list of numbers, change it into a balanced binary search tree.
You can assume there will be no duplicate numbers in the list.
'''

from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer


def createBalancedBST(nums):
  # print(nums)
  if len(nums) == 0:
    return None
  if len(nums) == 1:
    return Node(nums[0])

  mid = int(len(nums) / 2)  # middle index
  left_nums = nums[:mid] 
  right_nums = nums[mid+1:len(nums)]
  left = createBalancedBST(left_nums)
  right = createBalancedBST(right_nums)
  mid_node = Node(nums[mid], left, right)
  return mid_node

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7


# Some tests:

# null case
print(createBalancedBST([]))

# 1 case
print(createBalancedBST([1]))

# 2 case
print(createBalancedBST([1, 2]))
# ans: 21
#  2
# 1

# odd numbers
print(createBalancedBST([1,6,8]))
# ans: 168
#  6
# 1 8

# even numbers
print(createBalancedBST([1,3,6,8]))
# ans: 6381
#   6
#  3 8
# 1