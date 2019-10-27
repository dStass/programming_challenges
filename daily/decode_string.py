'''
Problem: Decode String 26/10/2019
Given a string with a certain rule:
k[string] should be expanded to string k times.

So for example, 3[abc] should be expanded to abcabcabc.
Nested expansions can happen,
so 2[a2[b]c] should be expanded to abbcabbc.
'''

def decodeString(s):
  NUMBERS = '1234567890'
  while '[' in s: # while still has brackets in it
    most_recent_open = -1
    for i in range(len(s)):
      if s[i] == '[':
        most_recent_open = i
      elif s[i] == ']':
        open_index = most_recent_open
        close_index = i

        # get index of '[' and the one before it will be a number
        num_repeat_len = 1
        while True:
          is_num = s[open_index-num_repeat_len]
          if is_num not in NUMBERS:
            break
          else:
            num_repeat_len += 1
        num_repeat_len -= 1

        num_repeat = int(s[open_index-num_repeat_len:open_index])

        # between opening bracket and closing
        repeated_str = s[open_index+1:close_index]

        # simple loop to create a decoded string
        replacement = ''
        for _ in range(num_repeat):
          replacement += repeated_str

        # replace string with everything before #[ and after ]
        s = s[0:open_index-num_repeat_len] + replacement + s[close_index+1:len(s)]
        break
  return s
  


print("1.", decodeString('9[a8[pb1[jo]]3[c]]'))
print("2.", decodeString('0[abc]'))
print("3.", decodeString('1[abc]'))
print("3.", decodeString('1[]'))
print("4.", decodeString('1[]6[b]'))
print("5.", decodeString('1[he]2[l]1[o world]'))
print("6.", decodeString('2[1[p]1[a]]1[r]1[a]2[z]1[i]')) # paparazzi
# abbcabbc
