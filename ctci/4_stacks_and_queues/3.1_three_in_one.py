# Describe how you could use a single array to implement three stacks.

# stack works by having the first n locations storing start of each stack
class NInOneStack:
  NUM_STACKS = 3
  STACK_START = "START"
  stack = None

  def __init__(self, num_stacks = 3):
    self.NUM_STACKS = num_stacks
    self.stack = list(range(self.NUM_STACKS, self.NUM_STACKS*2)) \
      + [self.STACK_START] * self.NUM_STACKS


  def push(self, num, val):
    if num < 1 or num > self.NUM_STACKS:
      return
    
    num -= 1
    stack_end_index = (num + 1) % self.NUM_STACKS

    stack_start = self.stack[num]
    stack_end = self.stack[stack_end_index]

    # reason for if else statement
    # we find the end of each individual stack eclusively by getting the start of the next start
    
    if stack_end_index != 0:
      self.stack = self.stack[:stack_end] + [val] + self.stack[stack_end:]
    else:
      self.stack.append(val)

    for i in range(num + 1, self.NUM_STACKS):
      self.stack[i] += 1
  

  def pop(self, num):
    if num < 1 or num > self.NUM_STACKS:
      return
    
    num -= 1
    stack_end_index = (num + 1) % self.NUM_STACKS

    stack_start = self.stack[num]
    index_to_pop =  self.stack[stack_end_index] - 1 \
                    if stack_end_index != 0 \
                    else len(self.stack) - 1

    if self.stack[index_to_pop] == self.STACK_START:
      return 'ERROR: EMPTY_STACK'
    
    to_return = self.stack.pop(index_to_pop)
    for i in range(num + 1, self.NUM_STACKS):
      self.stack[i] -= 1
    
    return to_return


  def stack_print(self):
    print(self.stack)



stack = NInOneStack()
# stack.stack_print()
# stack.push(2, 5)
# stack.stack_print()
# stack.push(2, 8)
# stack.stack_print()
# stack.push(3, 8)
# stack.stack_print()
# stack.push(1, 0)
# stack.stack_print()
# stack.push(3, 15)
# stack.stack_print()
# print(stack.pop(1))
# stack.stack_print()
# print(stack.pop(1))
# stack.stack_print()

stack.pop(1)
stack.push(1, 14)
stack.pop(1)
stack.push(1, 15)
# stack.pop(1)
stack.push(1, 16)



print(stack.pop(1))
print(stack.pop(1))
print(stack.pop(1))
print(stack.pop(1))
