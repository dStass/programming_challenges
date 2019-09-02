'''
Given a mathematical expression with just single digits,
plus signs, negative signs, and brackets, evaluate the expression.
Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4

'''
# LOGIC
# if there exists an opening parentheses (in a while loop)
# we read the expression from left to right and when
# a closing  bracket is found, we traverse backwards and
# when a matching opening bracket is found, get that substring
# should be in the form ( ... ) where ... here is a 'simple'
# expression, simple defined as not containing sub strings inside parantheses
# we replace this (...) block with a number
# and start again reading string from left to right
# we also handle cases where it is +(...) or -(...)
# and handle double negatives, etc
# when there is no longer any paranthesis in expression,
# it is now just a simple expression, we can use
# simple eval to evaluate final solutions

def eval(expr):
  expr = expr.replace(' ', '')
  while '(' in expr:
    for i in range(len(expr)):
      if expr[i] == ')':
        sub_expr = ""
        for j in range(i,-1, -1):
          sub_expr = expr[j] + sub_expr
          if expr[j] == '(':
            break

        before = expr[0:i - len(sub_expr)]
        sign = expr[i - len(sub_expr)]
        evaluated = simple_eval(sub_expr)
        after = expr[i+1:]

        if sign not in ['+', '-']:
          expr = expr[0:i - len(sub_expr) + 1] + evaluated + after
          break

        # evaluate scenarios where we have ++ -+ +- --n
        # ie double negatives = positive
        expr = before
        if sign == '+' and evaluated[0] == '-':
          expr += evaluated
        elif sign == '+' and evaluated[0] != '-':
          expr += '+' + evaluated
        elif sign == '-' and evaluated[0] == '-':
          expr += '+' + evaluated[1:]
        elif sign == '-' and evaluated[0] != '-':
          expr += '-' + evaluated
        expr += after
        break

  expr = simple_eval(expr)
  return int(expr) 

def simple_eval(expr):
  if len(expr) == 0:
    return ""
  
  # form (z1 + z2 + ...) or z1 + z2 + ...
  if expr[0] == '(':
    expr = expr[1:]
    expr = expr[:-1]
  
  # form -n1+n2-n3+ ... or n1+n2+n3-...
  # if expr[0] == '-':
  #   expr = '0' + expr  # convert -n1+... to 0-n1+...
  total = 0
  curr = "0"
  pos = True
  for i in range(len(expr)):
    if expr[i] in ['+', '-']:  # evaluate so far
      total += int(curr) if pos else -int(curr)
      curr = ""
      pos = True if expr[i] == '+' else False
      continue
    curr += expr[i]
  
  # last case
  total += int(curr) if pos else -int(curr)
  return str(total)

print(eval('- 1 + (3 + ( 2 - 1 + 3 + 5) + 8) + (1 - 2)')) # 18
print(eval('- ( 3 + ( 2 - 1 ) )')) # -4
print(eval('((1+2)-3)')) # 0
print(eval('((1+2+4))-(2+2+2-1)-2+5-(-1)')) # 6
print(eval('-(-1-(-1)-1)-(1-(-1))')) # -1
print(eval('-1')) # -1