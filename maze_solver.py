import tkinter as tk
import heapq
import random

# Parameters
SQUARE_SIZE = 42  # Adjust the size of each square
ANIMATION_SPEED = 150  # Milliseconds per animation step


class MazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = set()
        self.distances = {(i, j): float('inf')
                          for i in range(self.rows) for j in range(self.cols)}
        self.distances[start] = 0
        self.prev = {}
        self.queue = [(0, start)]

    def solve(self):
        while self.queue:
            dist, current = heapq.heappop(self.queue)
            if current == self.end:
                break
            if current in self.visited:
                continue
            self.visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    new_dist = dist + 1
                    if new_dist < self.distances[neighbor]:
                        self.distances[neighbor] = new_dist
                        self.prev[neighbor] = current
                        heapq.heappush(self.queue, (new_dist, neighbor))

    def get_neighbors(self, cell):
        i, j = cell
        neighbors = []
        if i > 0 and not self.maze[i - 1][j]:
            neighbors.append((i - 1, j))
        if i < self.rows - 1 and not self.maze[i + 1][j]:
            neighbors.append((i + 1, j))
        if j > 0 and not self.maze[i][j - 1]:
            neighbors.append((i, j - 1))
        if j < self.cols - 1 and not self.maze[i][j + 1]:
            neighbors.append((i, j + 1))
        return neighbors

    def reconstruct_path(self):
        path = []
        current = self.end
        while current != self.start:
            path.append(current)
            current = self.prev[current]
        path.append(self.start)
        return path[::-1]


class MazeGUI:
    def __init__(self, root, maze):
        self.root = root
        self.root.title("Maze Solver")
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.square_size = SQUARE_SIZE  # Adjust the size of each square
        self.animation_speed = ANIMATION_SPEED  # Milliseconds per animation step
        self.current_position = (0, 0)  # Initialize the current position

        self.canvas = tk.Canvas(
            root, width=self.cols * self.square_size, height=self.rows * self.square_size)
        self.canvas.pack()
        self.draw_maze()
        self.solve_maze()

    def draw_maze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                color = "white" if not self.maze[i][j] else "black"
                self.canvas.create_rectangle(
                    j * self.square_size, i * self.square_size, (j + 1) * self.square_size, (i + 1) * self.square_size, fill=color)

                if (i, j) == (0, 0):
                    self.canvas.create_rectangle(
                        j * self.square_size, i * self.square_size, (j + 1) * self.square_size, (i + 1) * self.square_size, fill="yellow"
                    )
                if (i, j) == (self.rows - 1, self.cols - 1):
                    self.canvas.create_rectangle(
                        j * self.square_size, i * self.square_size, (j + 1) * self.square_size, (i + 1) * self.square_size, fill="green"
                    )

    def solve_maze(self):

        while True:

            solver = MazeSolver(self.maze, (0, 0),
                                (self.rows - 1, self.cols - 1))
            solver.solve()

            try:
                path = solver.reconstruct_path()
                self.animate_path(path)
                break  # Break out of the loop if path reconstruction is successful
            except KeyError:  # Raised if goal is unreachable
                self.maze = generate_random_maze(self.rows, self.cols)
                self.draw_maze()
                self.current_position = (0, 0)  # Reset the current position

    def animate_path(self, path):
        for i, (row, col) in enumerate(path):
            x, y = col * self.square_size, row * self.square_size

            # Highlight the current square with a blue border
            if (row, col) != self.current_position:
                self.canvas.create_rectangle(
                    x, y, x + self.square_size, y + self.square_size, outline="blue", width=1)
                self.root.update()

            self.current_position = (row, col)  # Update the current position

            # Blinking effect for source (yellow) and goal (green) squares
            if (row, col) == (0, 0) or (row, col) == (self.rows - 1, self.cols - 1):
                for _ in range(3):  # Blink for 3 iterations
                    self.canvas.create_oval(
                        x + 5, y + 5, x + self.square_size - 5, y + self.square_size - 5, fill="blue")
                    self.root.update()
                    self.root.after(self.animation_speed)

                    self.canvas.delete("all")
                    self.draw_maze()
                    self.root.update()
                    self.root.after(self.animation_speed)
            else:
                self.canvas.create_oval(
                    x + 5, y + 5, x + self.square_size - 5, y + self.square_size - 5, fill="blue")
                self.root.update()
                self.root.after(self.animation_speed)

                if i < len(path) - 1:
                    self.canvas.create_line(
                        x + self.square_size // 2, y + self.square_size // 2, path[i + 1][1] * self.square_size + self.square_size // 2, path[i + 1][0] * self.square_size + self.square_size // 2, fill="blue", width=2)
                    self.root.update()
                    self.root.after(self.animation_speed)
                    self.canvas.delete("all")
                    self.draw_maze()

        # After the animation is finished, display the final path as a green line
        for i in range(len(path) - 1):
            row1, col1 = path[i]
            row2, col2 = path[i + 1]
            x1, y1 = col1 * self.square_size + self.square_size // 2, row1 * \
                self.square_size + self.square_size // 2
            x2, y2 = col2 * self.square_size + self.square_size // 2, row2 * \
                self.square_size + self.square_size // 2
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=2)
            self.root.update()
            self.root.after(self.animation_speed)


def generate_random_maze(rows, cols):
    maze = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 0  # Ensure the source remains open
    maze[rows - 1][cols - 1] = 0  # Ensure the goal remains open

    return maze


def main():

    maze_sizes = [3, 5, 10, 15]

    for maze_size in maze_sizes:
        rows = maze_size
        cols = maze_size
        maze = generate_random_maze(rows, cols)

        # Create the root window
        root = tk.Tk()

        # Center the maze on the screen
        x = (root.winfo_screenwidth() // 2) - (cols * SQUARE_SIZE // 2)
        y = (root.winfo_screenheight() // 2) - (rows * SQUARE_SIZE //
                                                2) - 50  # 50 accounts for the window title bar
        root.geometry(f"{cols * SQUARE_SIZE}x{rows * SQUARE_SIZE}+{x}+{y}")

        # Create the maze GUI
        gui = MazeGUI(root, maze)

        root.mainloop()


if __name__ == "__main__":
    main()