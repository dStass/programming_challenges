class Solution:
  def letterCombinations(self, digits):
    nmap = {
      '2':'abc',
      '3':'def',
      '4':'ghi',
      '5':'jkl',
      '6':'mno',
      '7':'pqrs',
      '8':'tuv',
      '9':'wxyz'
    }
    
    combinations = []
    d0 = digits[0]
    letters = nmap[d0]
    for l in letters:
      combinations.append(l)
    
    curr_digits = 1
    while curr_digits < len(digits):
      len_comb = len(combinations)
      for c in combinations.copy():
        for l in nmap[digits[curr_digits]]:
          combinations.append(c+l)
        # for d in digits[curr_digits:]:
        #   combinations.append(c+d)
      combinations = combinations[len_comb:]
      curr_digits += 1
    
    return sorted(list(set(combinations)))

print(Solution().letterCombinations('23'))