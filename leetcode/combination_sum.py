class Solution:
  def combinationSum(self, candidates, target):
    candidates.sort()
    solution = [ [] for i in range(target + 1)]
    for c in candidates:
      if c <= target:
        solution[c] = [[c]]
    print(solution)
    
    for i in range(1, target + 1):
      for c in candidates:
        if i - c <= 0:
          continue
        if len(solution[i-c]) == 0:
          continue
        possibles = solution[i-c]
        for p in possibles:
          new_sol = p[:]
          new_sol.append(c)
          new_sol.sort()
          if new_sol not in solution[i]:
            solution[i].append(new_sol)
    solution[target].sort()
    return solution[target]


sol = Solution().combinationSum([2,3,6,7], 7)
