'''
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    
    if len(grid) == 0:
      return 0
    self.GRID_WIDTH = len(grid)
    self.GRID_HEIGHT = len(grid[0])
    self.LAND = '1'
    self.WATER = '0'
    
    
    land = []
    water = []
    seen_cells = {}
    first = [0,0]
    land.append(first)
    
    seen_cells[self.coordinate_to_key(first)] = True
    previous_type = grid[0][0]
    num_islands = 0
    if previous_type == self.LAND:
      num_islands += 1
    
    while land or water:
      # print(queue)
      cell = None
      if land:
        cell = land.pop()
      else:
        cell = water.pop()
    
      cell_type = grid[cell[0]][cell[1]]
      
      if previous_type == self.WATER and cell_type == self.LAND:
        num_islands += 1
        
  
  
      surrounding_coordinates = self.get_surrounding_coords(cell)
      
        
      for s in surrounding_coordinates:
        s_key = self.coordinate_to_key(s)
        
        land_added = False
        if not seen_cells.get(s_key, False):
          
          s_type = grid[s[0]][s[1]]
          if s_type == self.LAND:
            if not land_added:
              land.append(s)
              seen_cells[s_key] = True
            land_added = True
          else:            
            water.append(s)
            seen_cells[s_key] = True
            
      
      previous_type = cell_type
      
      
      

    return num_islands
      
    
    
  
  def coordinate_to_key(self, coord):
    return '(' + str(coord[0]) + ',' + str(coord[1]) + ')'
  
  def get_surrounding_coords(self, cell):
    to_return = []
    cell_x = cell[0]
    cell_y = cell[1]
    for dif in [-1, 1]:
      new_x = cell_x + dif
      if new_x in range(0, self.GRID_WIDTH):
        to_return.append([new_x, cell_y])
    
    for dif in [-1, 1]:
      new_y = cell_y + dif
      if new_y in range(0, self.GRID_HEIGHT):
        to_return.append([cell_x, cell_y + dif])
    
    
    return to_return