
def get_max_encryptions(data):
  CHAR_LIMIT = 26
  size = len(data)
  max_messages = [0] * (size + 1)

  max_messages[size-1] = 1 # base case
  max_messages[size-2] = 2 if int(data[size-2:size]) in range(1, CHAR_LIMIT+1) else 1
  print("yos", max_messages[size-2], data[size-2:size])
  for i in range(size-2, -1, -1):
    if int(data[i:i+2]) in range(1, CHAR_LIMIT + 1):
      max_messages[i] = max_messages[i+2] + max_messages[i+1]
      print("yeetus", data[i:i+2], max_messages[i])
    else:
      print("yoop")
      max_messages[i] = max_messages[i+1]
    # if int(data[i]) 
    # print("yeet")
  # if len(data) == 0:
  #   return 1
  
  # if data[0] == 0:
  #   return 0

  # result = get_max_encryptions(data[1:])
  # if int(data[0:2]) in range(27):
  #   result += get_max_encryptions(data[2:])
  # return result
  # print(result)
  return "yo" + str(max_messages[0] + max_messages[1])





  
  # max_messages = [0] * size

  # # base case
  # max_messages[0] = 1 if data[0] != '0' else 0
  # if size == 1:
  #   return max_messages[0]
  
  # two_digits = int(data[0] + data[1])
  # if two_digits > 0 and two_digits < 27:
  #   max_messages[1] = max_messages[0] + 1
  # else:
  #   max_messages[1] = max_messages[0]
  
  # if size == 2:
  #   return max_messages[1]
  
  
  
  # for i in range(2, size):
    
  #   one_digit = (max_messages[i-1] + 1) if int(data[i]) > 0 else 0
    
  #   two_int = int(data[i-1]+data[i])
  #   two_digit = (max_messages[i-2] + 1) if (two_int > 0 and two_int < 27) else 0

  #   if one_digit == 0 and two_digit == 0:
  #     return 0
  #   max_messages[i] = one_digit + two_digit
  #   print("message=",max_messages[i])
  # return max_messages[size-1]

data = "12222232"

print("possible encryptions for", data, "=", get_max_encryptions(data))