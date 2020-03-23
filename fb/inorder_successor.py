class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 



def inorder(root):
  if not root:
    return

  inorder(root.left)
  print(root.val)
  inorder(root.right)

def inorder_successor(root_node, key):
  config = {
    "flag" : False,
    "successor": None
  }

  inorder_recursive(root_node, key, config)
  return config["successor"]
  

def inorder_recursive(root, key, config):
  if not root or config["successor"]:
    return

  inorder_recursive(root.left, key, config)

  if config["flag"]:
    config["successor"] = root
    config["flag"] = False

  if root.val == key:
    config["flag"] = True
  
  inorder_recursive(root.right, key, config)


root_1 = TreeNode(10)
root_1.left = TreeNode(7)
root_1.right = TreeNode(35)
root_1.left.left = TreeNode(5)
root_1.left.right = TreeNode(9)
root_1.right.left = TreeNode(30)
root_1.right.right = TreeNode(45)
print(inorder_successor(root_1, 5).val)