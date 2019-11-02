'''
Problem: Staying Put

You start at index 0 in an array with length 'h'.
At each step, you can move to the left,
move to the right, or stay in the same place
(Note: Stay in the same place also takes one step).
How many possible ways are you still at index 0 after you have walked 'n' step?

Example： n = 3
1. right->left->stay
2. right->stay->left
3. stay->right->left
4. stay->stay->stay
'''

class Solution:
  paths = None
  
  def __init__(self):
    self.paths = {}
    self.paths[0] = []
    self.paths[1] = ['s']
    self.paths[2] = ['lr','rl']

  def num_ways(self, n):
    return 0

s = Solution()

print(s.num_ways(0)) # 0
print(s.num_ways(1)) # 1 - s
print(s.num_ways(2)) # 2 - lr, rl
print(s.num_ways(3)) # 7 - lrs, rls, rsl, lsr, srl, slr, sss
# 4 - lrlr lrrl llrr | rllr rlrl rrll (6) + lrss + lsrs + lssr+ rlss, rsls + rssl + sslr + ssrl + ssss (9) = 15
# 5 - lrslr, lrlsr, llrsr, lrsrl, lrrsl


# . . .
# for num_ways(k):
# either: 
#    num_ways(k-1) and STAY
#     --> num_ways(k-1) + 1 WAYS
# OR
#    num_ways(k-2) and go right and left
#
#
