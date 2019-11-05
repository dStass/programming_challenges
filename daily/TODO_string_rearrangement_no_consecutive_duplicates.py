class CharCount:
  _letter = None
  _count = None

  def __init__(self, c):
    self._letter = c
    self._count = 0

  def __lt__(self, other):
    return self._count < other._count
  
  def __str__(self):
    return '[' + self._letter + ',' + str(self._count) + ']'

def rearrange_string(string):
  char_count_dict = {}
  char_count_list = []
  
  if len(string) == 0:  # empty
    return False
  
  if len(string) == 1:  # string with 1 char
    return True

  for i in range(len(string)):
    ci = string[i]
    cc = char_count_dict.get(ci, CharCount(ci))
    if cc._count == 0:
      cc._count += 1
      char_count_list.append(cc)  # insert in order
      char_count_dict[ci] = cc
    else:
      cc._count += 1
  
  char_count_list.sort()
  # for c in char_count_list:
  #   print(c)

  if len(char_count_list) < 2: # only 1 letter and not of length 1 (previously checked)
    return False

  half_list_size = int(len(string) / 2)

  window_start = 0
  window_end = 0
  
  sum_of_chars = char_count_list[0]._count
  if can_non_consec_be_formed(sum_of_chars, half_list_size, len(string)):
    return True

  while window_start < len(char_count_list):
    print(window_start, window_end)
    if window_end < len(char_count_list) - 1:
      window_end += 1
      sum_of_chars += char_count_list[window_end]._count
    else:
      sum_of_chars -= char_count_list[window_start]._count
      window_start += 1
    while sum_of_chars >= half_list_size:
      if can_non_consec_be_formed(sum_of_chars, half_list_size, len(string)):
        return True
      sum_of_chars -= char_count_list[window_start]._count
      window_start += 1

  return False





def has_consecutive_duplicates(string):
  if len(string) < 2:
    return False
  
  last = string[0]
  for i in range(1, len(string)):
    if string[i] == last:
      return True
    last = string[i]
  return False
  
def can_non_consec_be_formed(sum_of_chars, half_list_size, string_length):
  if string_length % 2 == 0:  # even
    if sum_of_chars == half_list_size or sum_of_chars == half_list_size + 1:
      return True
  else:
    if sum_of_chars == half_list_size or sum_of_chars == half_list_size + 1:
      return True
  return False

# print(has_consecutive_duplicates('abababa'))
  
# print(has_consecutive_duplicates('abaababa'))
print(rearrange_string('ababa'))
print(rearrange_string('abaababa'))
print(rearrange_string('abcabc'))
print(rearrange_string('acbccccabc'))