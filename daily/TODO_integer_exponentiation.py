'''
Implement integer exponentiation.
That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.
'''


# return x^y
def exp(x, y):
  base_pows = []
  p = 0
  x_p = x
  base_pows.append(x)
  while p + 2 <= y:
    p += 1
    x_p *= x
    base_pows.append(x_p)
  return base_pows

print(exp(2,16))