'''
Sort Stack:

Write a program to sort a stack such that the smallest items are on the top.

You can use an additional temporary stack,
but you may not copy the elements into any other data structure (such as an array).

The stack supports the following operations: push, pop, peek, and isEmpty.
'''

def sort_stack(stack):
  if stack == None:
    return None

  if len(stack) == 0:
    return stack
  
  sorted_stack = []
  sorted_stack.append(stack.pop())

  while stack:
    new_item = stack.pop()
    move_count = 0

    # traverse down the sorted stack and append it onto the given stack
    # keep a count of how many items we are transfering between both stacks
    # stop when items in stack is smaller than item to add
    while sorted_stack and new_item > sorted_stack[-1]:
      move_count += 1
      stack.append(sorted_stack.pop())
    
    sorted_stack.append(new_item)

    # transfer back what we've moved across
    for _ in range(move_count):
      sorted_stack.append(stack.pop())
  
  return sorted_stack


print(sort_stack([1,2,3,4, 8, 0, 19, 0, 25, 3, 5,19]))
print(sort_stack([0]))
print(sort_stack([]))
print(sort_stack(None))