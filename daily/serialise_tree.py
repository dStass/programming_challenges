'''
From: Daily Coding Problem 31/08/2019
Problem: Serialise and Deserialise a tree

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# recursion:
# either node is None or a node
# if None, return "None"
# else return from [val, leftNode, rightNode]
# ASSUMPTION: NO commas ',' in names
def serialise(node):
  if node == None:
    return "None"
  to_return = "["
  to_return += str(node.val)
  to_return += ","
  to_return += serialise(node.left)
  to_return += ","
  to_return += serialise(node.right)
  to_return += "]"
  return to_return

# 'peel' off layers 
def deserialise(s):
  if s == "None":
    return None
  s_split = split_str(s)
  val = s_split[0]
  left = s_split[1]
  right = s_split[2]
  to_return = Node(val, deserialise(left), deserialise(right))
  return to_return


# form: [val, left, right] where left = [...] and right = [...]
def split_str(s):
  # remove first and last brackets
  s = s[1:]
  s = s[:-1]
  
  to_return = []
  bracket_stack = 0
  curr = ""
  for c in s:
    curr += c
    if c == '[':
      bracket_stack += 1
    if c == ']':
      bracket_stack -= 1
    if c == ',' and bracket_stack == 0:
      to_return.append(curr[:-1])
      curr = ""
  to_return.append(curr)
  return to_return
  

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialise(node))
assert deserialise(serialise(node)).left.left.val == 'left.left'