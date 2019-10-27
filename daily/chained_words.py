'''
Problem: Circle of Chained Words 27/10/2019
Two words can be 'chained' if the last character of the first word
is the same as the first character of the second word. 

Given a list of words, determine if there is a way to 'chain'
all the words in a circle.

Example:
Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True
Explanation:
The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna']
creates a circle of chained words.

'''
class State:
  def __init__(self, so_far, to_go):
    self._so_far = so_far
    self._to_go = to_go
    self._curr = so_far[len(so_far) - 1] if len(so_far) > 0 else ''

    self.string_value = ''
    for s in so_far:
      self.string_value += s
  
  def __str__(self):
    return self.string_value

  def str_reverse(self):
    reverse = ''
    for s in self._so_far[::-1]:
      reverse += s
    return reverse


def chainedWords(words):
  for i in range(len(words)):   
    seen = {}
    first_state = State([words[i]], words[0:i]+words[i+1:len(words)])
    to_explore = []
    to_explore.append(first_state)
    while to_explore:
      curr = to_explore.pop()
      seen[str(curr)] = True

      if len(curr._to_go) == 0:
        return curr._so_far
      
      for j in range(len(curr._to_go)):
        next_word = curr._to_go[j]
        if not seen.get(str(next_word), False):
          curr_word = curr._curr
          if canChain(curr_word, next_word):
            next_so_far = curr._so_far.copy()
            next_so_far.append(next_word)

            next_to_go = curr._to_go[0:j] + curr._to_go[j+1:len(curr._to_go)]
            next = State(next_so_far, next_to_go)
            to_explore.append(next)
  return None

def canChain(first, second):
  if second[0] == first[len(first) - 1]:
    return True
  else:
    return False
        
        


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
print(chainedWords(['tunap', 'karat', 'snack', 'eggs', 'paul']))
print(chainedWords(['abc']))
print(chainedWords([]))
print(chainedWords(['abc', 'oba']))
print(chainedWords(['abc', 'obo']))