'''
Given a binary tree, get the average value at each level of the tree
'''
from heapq import *


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def get_level_average(root):
  to_return = []
  queue = []
  queue.append(root)

  num_nodes_at_level = 1
  num_nodes_left_at_level = 1

  running_sum = 0
  while queue:
    curr = queue.pop(0)
    num_nodes_left_at_level -= 1
    running_sum += curr.val

    if curr.left:
      queue.append(curr.left)
    
    if curr.right:
      queue.append(curr.right)



    if num_nodes_left_at_level == 0:
      # print(running_sum)
      to_return.append(running_sum/num_nodes_at_level)

      num_nodes_at_level = len(queue)
      num_nodes_left_at_level = num_nodes_at_level
      running_sum = 0

  return to_return

root = Node(4.0)

root.left = Node(7.0)
root.left.left = Node(10.0)
root.left.right = Node(2.0)
root.left.right.right = Node(6.0)
root.left.right.right.left = Node(2.0)

root.right = Node(9.0)
root.right.right = Node(6.0)

print(get_level_average(root))

pq = [10, 2, 60, 14]
# heappush(pq, 10)
# heappush(pq, 2)
# heappush(pq, 60)
# heappush(pq, 14)
print(heappop(pq))