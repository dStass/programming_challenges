'''
From: Daily Interview Pro 22/08/19
Problem: Reverse a Linked List

Given a singly-linked list, reverse the list.
This can be done iteratively or recursively. Can you get both solutions?
'''

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  # Function to print the list
  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    size = 1
    curr = head
    while (curr != None):
      next = curr.next
      curr.next = None if size == 1 else prev
      prev = curr
      curr = next
      size += 1

  # Recursive Solution
  def reverseRecursively(self, head):
    if head == None:
      return head
    if head.next == None:
      return head
    head.reverseRecursively(head.next)
    head.next.next = head
    head.next = None


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
# testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
