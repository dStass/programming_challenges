def first_recurring(input_string):
  seen = {}
  for c in input_string:
    found = seen.get(c, False)
    if found:
      return c
    else:
      seen[c] = True
  return None

print(first_recurring('abcdefghcgah'))