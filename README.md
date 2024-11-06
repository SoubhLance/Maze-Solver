# Maze Solver Using Dijkstra's Algorithm

Project Overview
This project implements a Maze Solver using Dijkstra's Algorithm to find the shortest path from the start to the goal in a maze. Dijkstra’s algorithm is a graph traversal technique that guarantees the shortest path in a weighted graph, making it an ideal choice for solving mazes.

![image](https://github.com/user-attachments/assets/4d274b66-f7d3-48fa-8758-aa13e5072aa8)

Key Features:
Solves mazes of varying difficulty levels.
Visualizes the process of finding the shortest path.
Utilizes Dijkstra’s algorithm for pathfinding in the maze.

#Table of Contents
-Usage
-Algorithm Overview
-Time Complexity

#Usage
- Run the Maze Solver:
   - python maze_solver.py
   - The program will visualize the maze and the pathfinding process.
- Input Maze:
  - The maze can be provided as an input file, or you can generate random mazes using a built-in generator.
- View Results:
  - After the algorithm runs, the solution path will be highlighted, showing the optimal path from start to goal.
 
#Algorithm Overview
#Dijkstra’s Algorithm:
Dijkstra’s algorithm is a greedy algorithm used to find the shortest path between nodes in a graph. The algorithm works by selecting the node with the smallest tentative distance and updating the distances to its neighbors. This process is repeated until the destination node is reached.

Steps involved:

-Initialize all nodes with an infinite distance, except for the start node (set to 0).
-Choose the node with the smallest tentative distance.
-Update the tentative distance of its neighbors.
-Repeat until the goal node is reached or all nodes have been visited.

#Time Complexity
- Adjacency Matrix Representation:
  O(V²) where V is the number of vertices (nodes).

- Adjacency List & Priority Queue (Min-Heap):
  O((V + E) * log V) where V is the number of vertices and E is the number of edges. This is more efficient for sparse graphs.

#End of README

![image](https://github.com/user-attachments/assets/b68c35d5-1930-495d-9cea-60a12dc9b8b0)
![image](https://github.com/user-attachments/assets/4d122911-63ed-427b-a36a-3a36bd0fdf6d)
![image](https://github.com/user-attachments/assets/081db3e0-59c5-45e8-8372-9ec188ad5516)
![image](https://github.com/user-attachments/assets/6f2fa7ab-4a85-4c34-b2da-f4d080d07133)
![image](https://github.com/user-attachments/assets/4d274b66-f7d3-48fa-8758-aa13e5072aa8)




