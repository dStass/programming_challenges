'''
Problem: Look and say sequence
From: Coding Interview Pro 27/09/2019

A look-and-say sequence is defined as the integer sequence beginning
with a single digit in which the next term is obtained by describing the previous term.
An example is easier to understand:

Each consecutive value describes the prior value.
1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
'''

def look_and_say(n):
  if n == 0:
    return ""
  seq = "1"
  for _ in range(1,n):
    new_seq = ""
    c = seq[0]
    count = 1
    for ci in range(1,len(seq)):  # char index
      c = seq[ci]
      if c == seq[ci-1]:
        count += 1
      else:
        new_seq += str(count) + str(seq[ci-1])
        count = 1
    new_seq += str(count) + str(seq[len(seq) - 1])
    seq = new_seq
  return seq

# tests
print(look_and_say(0))
print(look_and_say(1))
print(look_and_say(2))
print(look_and_say(3))
print(look_and_say(4))
print(look_and_say(5))
print(look_and_say(6))
print(look_and_say(7))
print(look_and_say(8))
print(look_and_say(9))
