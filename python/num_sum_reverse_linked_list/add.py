'''
From: Daily Interview Pro 17/08/2019
Problem: Add Two Numbers as a Linked List

You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    num1 = self.getNumFromList(l1)
    num2 = self.getNumFromList(l2)
    result = num1 + num2
    return self.getListFromNum(result)

  def getNumFromList(self, l):
    to_return = 0
    i = 0
    while l:
      to_return += l.val * pow(10, i)  # l.val * 10^(i)
      l = l.next
      i += 1
    return to_return

  def getListFromNum(self, n):
    i = 1
    to_return = ListNode(0)
    curr_node = to_return
    while (n > 0):
      mod_by = pow(10, i)
      remainder = n % mod_by
      n -= remainder
      remainder /= pow(10, i-1)
      curr_node.val = int(remainder)
      if n > 0:
        curr_node.next = ListNode(0)
        curr_node = curr_node.next
      i += 1
    return to_return



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
