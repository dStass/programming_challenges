'''
From Atlassian online coding test
Problem found again online

Lara owns a flower shop, where she sells only two types of flower bouquets:

Type 1: the first type of bouquet contains three roses and costs p dollars.
Type 2: The second type of bouquet contains one cosmos and one rose and costs q dollars.
Lara grows these flowers in her own garden in a single row.

Consider the row as a one-dimensional array, here each cell either contains a rose or a cosmos.
For example array 001101011, here 0 indicates rose and 1 indicates cosmos.

Lara follows an important rule when she makes the bouquets:
she makes each bouquet with only consecutive flowers from the array.

For example in a bouquet, the flower from consecutive (i, i+1, and i+2) in the array can be present,
but not from non-consecutive indices (i and i+2) in the array above,
Lara can not make any bouquets of type 1 but she can make 3 bouquets of type 2

Now she wonder what is the maximum profit she can make if she makes these bouquets optimally.
You are given a binary string representing her garden row. calculate the maximum profit Lara can make.
Remember that it is not necessary to use every flower


The function must return an integer that denotes the maximum profit Lara can make if she makes her bouquet optimally.
'''

import sys

# garden = string 
# roses = 000, costs p
# cosmos = 01 or 10, costs q

# Solved with dynamic programming in O(N) time
# start with index 1
# contain a list of best cost up to index
# at every index, check if it ends with 000 or 01|10 
# add costs p or q respectively and check if it's bigger than 
# at index i - 1 or i - 2 as well in roses (000) case
# if it is bigger add it as the largest
# else get i-1 biggest size and add that
def max_profit(garden, p, q):
  gsize = len(garden)
  sub_maxl = [0]*gsize
  for i in range(1, gsize):
    roses = 0
    cosmos = 0
    if i > 1 and garden[i-2:i+1] == "000":
      roses = (sub_maxl[i-3] if i > 2 else 0) + p
      sub_maxl[i] = max(sub_maxl[i-2], sub_maxl[i-1], roses)
    elif garden[i-1:i+1] in {"01", "10"}:
      cosmos = (sub_maxl[i-2] if i > 1 else 0) + q
      sub_maxl[i] = max(sub_maxl[i-1], cosmos)
    else:
      sub_maxl[i] = sub_maxl[i-1]
    print(i, " ", sub_maxl, " ", sep='', end='')
    print("roses" if roses > 0 else ("cosmos" if cosmos > 0 else "none"))
  return sub_maxl[gsize-1]

garden = sys.argv[1]
p = int(sys.argv[2])
q = int(sys.argv[3])

print("max prof is: ", max_profit(garden, p, q), sep='')