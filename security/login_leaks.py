class Node:
  def __init__(self, val):
    self.val = val
    self.left_set = set()
    self.right_set = set()
  
  def __str__(self):
    return str(self.val) + ' pos: ' + str(len(self.left_set))

class Solution:
  def __init__(self, file_name):
    self.fragments = []
    self.nodes = {}
    self.lefts = {}
    self.rights = {}

    self.getFragmentsFromFile(file_name)
    self.build_relative_position()
    self.form_solution()
  
  def getFragmentsFromFile(self, file_name):
    fp = open(file_name, 'r')
    line = fp.readline()

    while line:
      if len(line) > 3:
        line = line[:-1]
      self.fragments.append(line)
      mid_c = line[1]
      left_c = line[0]
      right_c = line[2]

      if mid_c not in self.nodes:
        self.nodes[mid_c] = Node(mid_c)

      if left_c not in self.nodes:
        self.nodes[left_c] = Node(left_c)

      if right_c not in self.nodes:
        self.nodes[right_c] = Node(right_c)

      # middle one has one left and one right
      self.nodes[mid_c].left_set.add(left_c)
      self.nodes[mid_c].right_set.add(right_c)

      # left one will have the other two to its right
      self.nodes[left_c].right_set.add(mid_c)
      self.nodes[left_c].right_set.add(right_c)

      # right one will have the first two to its left
      self.nodes[right_c].left_set.add(left_c)
      self.nodes[right_c].left_set.add(mid_c)

      line = fp.readline()


  # get all nodes positioned to the left of a node
  # then for each of those, get all the nodes to its left
  # build a set for each node that contains every single node to its left
  # repeat for its right
  # eg: given a word 'pear'
  # and two fragments 'pea' and 'ear'
  #
  # from this we know that r has 'e' and 'a' to its left
  # but both 'e' and 'a' contains 'p' to its left
  # can join 'a' into 'r''s left_set
  # ie Node('r').left_set = {'p', 'e', 'a'}
  #
  # re cursively do this for all nodes on either side of each node
  # this can be computationally expensive, so, we memoize a node's left_set if 
  # we have already done calculations on it
  # similarly, repeat for right nodes
  def build_relative_position(self):
    for n in self.nodes:
      self.generate_left(self.nodes[n])
      self.generate_right(self.nodes[n])
    
    for n in self.nodes:
      node = self.nodes[n]
      node.left_set = self.lefts[n]
      node.right_set = self.rights[n]
    
  def generate_left(self, node):
    if node.val in self.lefts:
      return self.lefts[node.val]
    all_lefts = set().union(node.left_set)
    for l in node.left_set:
      if l not in self.nodes:
        continue
      node_left = self.generate_left(self.nodes[l])
      if node_left:
        all_lefts = all_lefts.union(node_left)
    self.lefts[node.val] = all_lefts
    return self.lefts[node.val]

  def generate_right(self, node):
    if node.val in self.rights:
      return self.rights[node.val]
    all_rights = set().union(node.right_set)
    for l in node.right_set:
      if l not in self.nodes:
        continue
      node_right = self.generate_right(self.nodes[l])
      if node_right:
        all_rights = all_rights.union(node_right)
    self.rights[node.val] = all_rights
    return self.rights[node.val]
  

  # at this stage, every node should have a set containing nodes to its left
  # and another set containing nodes to its right
  # we can recognise here that a node with it's left_set of size 0 will
  # be the first node, a nodes with left_set of size 1 will be the second, etc. 
  # we put this into a tuple and sort based on number of items to a node's left
  # return a string of the solution
  def form_solution(self):
    tuples = [] # list of tuples containing pairs where first item = number of items to the node's left and second value is the node's name
    for n in self.nodes:
      node = self.nodes[n]
      tuples.append((len(node.left_set), node.val))

    tuples.sort()
    solution = []
    for t in tuples:
      solution.append(t[1])
    self.solution = ''.join(solution)
    # self.solution = ''.join([t[1] for t in sorted([tuples])])

  def get_solution(self):
    return self.solution

  def print(self):
    for n in self.nodes:
      node = self.nodes[n]
      print(node)
      
sol = Solution('fragments.txt')
print(sol.get_solution())
