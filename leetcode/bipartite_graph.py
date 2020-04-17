class Solution:

  def isBipartite(self, graph):
    COLOUR_0 = 0
    COLOUR_1 = 1
    
    colours = {}
    to_search = {}

    for i in range(len(graph)):
      to_search[i] = i



    prev_colour = None
    current_colour = COLOUR_0

    queue = []
    queue.append(0)
    
    num_at_depth = 1
    while queue or len(to_search) > 0:
      if not queue:
        val = None
        for k in to_search:
          val = k
          break
        queue.append(val)
        num_at_depth = 1

      curr = queue.pop(0)
      if curr not in colours:
        colours[curr] = current_colour
        del to_search[curr]

      for neighbour in graph[curr]:
        if neighbour not in colours:
          if neighbour not in queue:
            queue.append(neighbour)
        else:
          if colours[neighbour] == current_colour:
            return False
      
      num_at_depth -= 1
      if num_at_depth == 0:
        num_at_depth = len(queue)
        prev_colour = current_colour
        current_colour = COLOUR_1 if current_colour == COLOUR_0 else COLOUR_0
      
      
    return True
  

graph = [[1],[0],[4],[4],[2,3]]
s = Solution()
print(s.isBipartite(graph))