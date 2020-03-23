'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

'''

import random


class Graph:
  adj = None
  connections = None

  def __init__(self, vertices = 5, edges = 4):
    self.SIZE = vertices
    self.graph_generator(vertices, edges)



  def graph_generator(self, size, num_connections):
    connections = []
    while len(connections) != num_connections:
      new_connection = []
      random_x = random.randint(0, size-1)
      random_y = random.randint(0, size-1)
      new_connection.append(random_x)
      new_connection.append(random_y)

      new_connection = sorted(new_connection)
      if new_connection not in connections and random_x != random_y:
        connections.append(new_connection)


    adj = []
    for _ in range(size):
      adj.append([0] * size)
    
    for c in connections:
      row = c[0]
      col = c[1]
      adj[row][col] = 1
      adj[col][row] = 1

    self.adj = adj
    self.connections = connections

  def print(self):
    for i in range(self.SIZE):
      print(self.adj[i])
    

g = Graph(10, 20)
g.print()