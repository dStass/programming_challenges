
def get_max_encryptions(data):
  CHAR_LIMIT = 26
  size = len(data)
  max_messages = [0] * (size + 1)

  max_messages[size-1] = 1 # base case
  max_messages[size-2] = 2 if int(data[size-2:size]) in range(1, CHAR_LIMIT+1) else 1
  for i in range(size-2, -1, -1):
    if data[i] == '0':
      if i == 0: 
        return 0
      elif int(data[i-1]) not in range(1,3):
        return 0 
    max_messages[i] = max_messages[i+1]
    if int(data[i:i+2]) in range(1, CHAR_LIMIT + 1):
      max_messages[i] += max_messages[i+2]
  return max_messages[0]


def helper(data, k):
  if k == 0:
    return 1
  s = len(data) - k
  if data[s] == '0':
    return 0
  
  result = helper(data, k-1)
  if k >= 2 and int(data[s:s+2]) <= 26:
    result += helper(data, k-2)
  return result

def num_ways(data):
  return helper(data, len(data))


data = "1232205"

print("possible encryptions for", data, "=", get_max_encryptions(data))

