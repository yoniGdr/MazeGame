from maze import Maze


class Solver():
    """
    Class that solves the maze using the BFS algorithm
    """

    def __init__(self, maze: Maze):
        """
        Constructor for the Solver class
        :param maze: The maze to be solved
        """
        self.class_maze = maze
        self.maze = maze.get_matrix_maze()
        self.start =  maze.get_start()
        self.end = maze.get_end()
        self.solved_maze = []
        self.path_to_end = []
        self.movements = []
        self.init_solved_maze()
        self.solve()
        self.translate_path()


    def change_target(self,start,end):
        self.start = start
        self.end =  end
        self.solved_maze = []
        self.path_to_end = []
        self.movements = []
        self.init_solved_maze()
        self.solve()
        self.translate_path()


    def make_step(self,step):
        """
        Makes a step in the maze
        :param step: The step to be made
        """

        for i in range(len(self.solved_maze)):
            for j in range(len(self.solved_maze[i])):
                if self.solved_maze[i][j] == step:
                    if i>0 and self.solved_maze[i-1][j] == 0 and self.maze[i-1][j] == 0:
                     self.solved_maze[i-1][j] = step + 1
                    if j>0 and self.solved_maze[i][j-1] == 0 and self.maze[i][j-1] == 0:
                     self.solved_maze[i][j-1] = step + 1
                    if i<len(self.solved_maze)-1 and self.solved_maze[i+1][j] == 0 and self.maze[i+1][j] == 0:
                     self.solved_maze[i+1][j] = step + 1
                    if j<len(self.solved_maze[i])-1 and self.solved_maze[i][j+1] == 0 and self.maze[i][j+1] == 0:
                      self.solved_maze[i][j+1] = step + 1

    def print_maze(self):
        """
        Prints the maze
        """
        for i in range(len(self.solved_maze)):
            for j in range(len(self.solved_maze[i])):
                print("("+str(i)+","+str(j)+") :"+str(self.solved_maze[i][j]).ljust(2),end=' ')
            print()
    
    def init_solved_maze(self): 
        """
        Initializes the solved maze
        """
        for i in range(len(self.maze)):
            self.solved_maze.append([])
            for j in range(len(self.maze[i])):
                self.solved_maze[-1].append(0)
        i,j = self.start
        self.solved_maze[i][j] = 1

    def get_previous_step(self, cell):
        """
        Gets the previous step

        :param cell: The cell to get the previous step from
        :return: The previous step
        """

        neighbors = self.get_neighbors(cell)

        previous_step = cell
        for neighbor in neighbors:
            
            if self.solved_maze[neighbor[0]][neighbor[1]] < self.solved_maze[previous_step[0]][previous_step[1]]:
                previous_step = neighbor
                break

        return previous_step

     
    def get_neighbors(self, cell):
        """
        Gets the neighbors of a cell
        :param cell: The cell to get the neighbors from
        :return: The neighbors of the cell
        """
        i, j = cell
        neighbors = []
        if i > 0 and self.solved_maze[i - 1][j] != 0:
            neighbors.append((i - 1, j))
        if j > 0 and self.solved_maze[i][j - 1] != 0:
            neighbors.append((i, j - 1))
        if i < len(self.solved_maze) - 1 and self.solved_maze[i + 1][j] != 0:
            neighbors.append((i + 1, j))
        if j < len(self.solved_maze[i]) - 1 and self.solved_maze[i][j + 1] != 0:
            neighbors.append((i, j + 1))
        return neighbors

        
    def get_solved_maze(self):
        """
        Gets the solved maze
        :return: The solved maze
        """
        return self.solved_maze

    def get_cell(self,x,y):
        """
        Gets the cell in the maze
        :param x: The x coordinate of the cell
        :param y: The y coordinate of the cell
        :return: The cell
        """
        return self.solved_maze[x][y]
    
    def is_cell(self,cell):
        """
        Checks if a cell is in the maze
        :param cell: The cell to check
        :return: True if the cell is in the maze, False otherwise
        """
        return self.solved_maze[cell[0]][cell[1]] != 0

    def translate_path(self): #TODO
        """
        Translates the path to the end of the maze
        the translaton is done by adding "U" for up, "D" for down, "L" for left and "R" for right
        """
        cache = self.path_to_end.copy()
        cache.insert(0,None)
        previous = cache.pop()
        next_c = None
        while previous != None:
            
            next_c = cache.pop()
            if(next_c == None):
                break
            if( previous[0] == next_c[0]):
                if(previous[1]<next_c[1]):
                    self.movements.append("right")
                else:
                    self.movements.append("left")
            elif (previous[0] > next_c[0]):
                self.movements.append("up")
            else:
                self.movements.append("down")
            previous = next_c

    def get_movements(self):
        """
        Gets the movements
        :return: The movements
        """
        return self.movements

    def solve(self):
        """
        Solves the maze
        """
        
        step = 0
        while self.solved_maze[self.end[0]][self.end[1]] == 0:
            step += 1
            self.make_step(step)

        i, j = self.end
        step = self.solved_maze[i][j]
        self.path_to_end = [(i,j)]
        while step > 1:
              if i > 0 and self.solved_maze[i - 1][j] == step-1:
                i, j = i-1, j
                self.path_to_end.append((i, j))
                step-=1
              elif j > 0 and self.solved_maze[i][j - 1] == step-1:
                i, j = i, j-1
                self.path_to_end.append((i, j))
                step-=1
              elif i < len(self.solved_maze) - 1 and self.solved_maze[i + 1][j] == step-1:
                i, j = i+1, j
                self.path_to_end.append((i, j))
                step-=1
              elif j < len(self.solved_maze[i]) - 1 and self.solved_maze[i][j + 1] == step-1:
                i, j = i, j+1
                self.path_to_end.append((i, j))
                step -= 1


if __name__ == "__main__":
    maze = Maze(10,10)
    maze.print_maze()
    solver = Solver(maze)
    print(" start : ",maze.get_start())
    print(" end : ",maze.get_end())
    solver.print_maze()
