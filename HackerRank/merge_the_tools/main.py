# split string into k parts
# remove duplicates by using set
def merge_the_tools(string, k):
  n = len(string)
  to_return = []
  for i in range(0, n, k):
    sub_str = string[i:i+k]
    fixed_str = ""
    seen = {}
    for c in sub_str:
      found = seen.get(c, False)
      if not found:
        fixed_str += c
        seen[c] = True
    to_return.append(fixed_str)
  return to_return

if __name__ == '__main__':
    string, k = input(), int(input())
    print(merge_the_tools(string, k))