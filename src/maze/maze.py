## Imports
import random


## Global Variables
WALL = '0' # represents a wall
CELL = '1' # represents a cell
UNVISITED = '-1' # represents an unvisited cell

class Maze:
    """
    Class that represents a maze :
    - The maze is represented as a list of lists
    - The maze is a list of rows
    - Each row is a list of cells
    - Each cell is a list of walls
    - Each wall is a tuple of (x, y) coordinates
    """

    def __init__(self, width, height):
        """
        Constructor of the class Maze

        :param width: width of the maze
        :param height: height of the maze
        """
        if(width < 5 or height < 5):
            raise Exception("min width and height : 5")
        self.width = width
        self.height = height
        self.maze = []
        self.matrix_maze = []
        self.set_unvisited_cells()
        self.set_start()
        self.generate_maze()
        self.generate_matrix()


    def get_width(self):
        """
        Gets the width of the maze

        :return: width of the maze
        """
        return self.width

    def get_height(self):
        """
        Gets the height of the maze

        :return: height of the maze
        """
        return self.height

    def get_start(self):
        """
        Returns the coordinates of the start of the maze

        :return: (y, x)
        """
        for i in range(self.width):
            if(self.maze[0][i] == CELL):
                return (0,i)
        return None

    def is_wall(self,x,y):
        """
        Checks if the cell (x,y) is a wall

        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :return: True if the cell is a wall, False otherwise
        """

        return self.maze[x][y] == WALL

    def get_end(self):
        """
        Returns the coordinates of the end of the maze

        :return: (y, x)
        """
        for i in range(self.width):
            if(self.maze[self.height-1][i] == CELL):
                return (self.height-1, i)
        return None

    def get_maze(self):
        """
        Returns the maze as a list of lists

        :return: the maze as a list of lists
        """
        return self.maze

    def print_maze(self):
        """
        Prints the maze
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.maze[i][j], end=' ')
            print('\n')

    def remove_random_walls(self,nb_walls):
        """
        Removes a given number of walls from the maze

        :param nb_walls: nb_walls to remove
        """
        i=0
        while i < nb_walls:
            y = int(random.random() * self.height)
            x = int(random.random() * self.width)
            if (y == 0):
                y += 1
            if (y == self.height - 1):
                y -= 1
            if (x == 0):
                x += 1
            if (x == self.width - 1):
                x -= 1
            if self.is_wall(y,x):
                self.maze[y][x]= CELL
                i+=1



        

    def generate_matrix(self):
        """
        Generates the matrix of the maze
        """
        row = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.maze[i][j] == CELL:
                    row.append(0)
                else:
                    row.append(1)
            self.matrix_maze.append(row)
            row = []
    
    def get_matrix_maze(self):
        """
        Gets the matrix of the maze

        :return: the matrix of the maze
        """
        return self.matrix_maze
        
    def nb_neighbors(self,random_wall):
        """
        Returns the number of neighbors of a wall

        :param random_wall: a wall
        :return: the number of neighbors of a wall
        """
        cells_cache = 0
        if (self.maze[random_wall[0]-1][random_wall[1]] == CELL):
            cells_cache += 1
        if (self.maze[random_wall[0]+1][random_wall[1]] == CELL):
            cells_cache += 1
        if (self.maze[random_wall[0]][random_wall[1]-1] == CELL):
            cells_cache +=1
        if (self.maze[random_wall[0]][random_wall[1]+1] == CELL):
            cells_cache += 1

        return cells_cache


    def set_unvisited_cells(self):
        """
        Sets all the cells to unvisited
        """
        for _ in range(0, self.height):
            line = []
            for _ in range(0, self.width):
                line.append(UNVISITED)
            self.maze.append(line)


    def get_random_cell(self):
        """
        Gets a random cell

        :return: (y, x)
        """
        random_cell = (random.randint(0, self.height-1), random.randint(0, self.width-1))
        while(self.maze[random_cell[0]][random_cell[1]] != CELL):
            random_cell = (random.randint(0, self.height-1), random.randint(0, self.width-1))
        if random_cell == (self.start_y, self.start_x) or (random_cell[0]< 5 and random_cell[1] < 5): 
            return self.get_random_cell()
        else:
            return random_cell

    # Randomize starting point and set it a cell
    def set_start(self):
        """
        Sets the starting point of the maze
        """
        self.start_y = int(random.random()*self.height)
        self.start_x = int(random.random()*self.width)
        if (self.start_y == 0):
            self.start_y += 1
        if (self.start_y == self.height-1):
            self.start_y -= 1
        if (self.start_x == 0):
            self.start_x += 1
        if (self.start_x == self.width-1):
            self.start_x -= 1

    def generate_maze(self):
        """
        Generates the maze
        """

        self.maze[self.start_y][self.start_x] = CELL
        walls = []
        walls.append([self.start_y - 1, self.start_x])
        walls.append([self.start_y, self.start_x - 1])
        walls.append([self.start_y, self.start_x + 1])
        walls.append([self.start_y + 1, self.start_x])

        # Denote walls in maze
        self.maze[self.start_y-1][self.start_x] = WALL
        self.maze[self.start_y][self.start_x - 1] = WALL
        self.maze[self.start_y][self.start_x + 1] = WALL
        self.maze[self.start_y + 1][self.start_x] = WALL

        while (walls):
            # Pick a random wall
            random_wall = walls[int(random.random()*len(walls))-1]

            # Check if it is a left wall
            if (random_wall[1] != 0):
                if (self.maze[random_wall[0]][random_wall[1]-1] == UNVISITED and self.maze[random_wall[0]][random_wall[1]+1] == CELL):
                    # Find the number of surrounding cells
                    cells_cache = self.nb_neighbors(random_wall)

                    if (cells_cache < 2):
                        # Denote the new path
                        self.maze[random_wall[0]][random_wall[1]] = CELL

                        # Mark the new walls
                        # Upper cell
                        if (random_wall[0] != 0):
                            if (self.maze[random_wall[0]-1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]-1][random_wall[1]] = WALL
                            if ([random_wall[0]-1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]-1, random_wall[1]])


                        # Bottom cell
                        if (random_wall[0] != self.height-1):
                            if (self.maze[random_wall[0]+1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]+1][random_wall[1]] = WALL
                            if ([random_wall[0]+1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]+1, random_wall[1]])

                        # Leftmost cell
                        if (random_wall[1] != 0):	
                            if (self.maze[random_wall[0]][random_wall[1]-1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]-1] = WALL
                            if ([random_wall[0], random_wall[1]-1] not in walls):
                                walls.append([random_wall[0], random_wall[1]-1])
                    

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                            walls.remove(wall)

                    continue

            if (random_wall[0] != 0):
                if (self.maze[random_wall[0]-1][random_wall[1]] == UNVISITED and self.maze[random_wall[0]+1][random_wall[1]] == CELL):

                    cells_cache = self.nb_neighbors(random_wall)
                    if (cells_cache < 2):

                        self.maze[random_wall[0]][random_wall[1]] = CELL

                        if (random_wall[0] != 0): # Check if it is not the top row
                            if (self.maze[random_wall[0]-1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]-1][random_wall[1]] = WALL
                            if ([random_wall[0]-1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]-1, random_wall[1]])

                        if (random_wall[1] != 0): # Check if it is not the leftmost column
                            if (self.maze[random_wall[0]][random_wall[1]-1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]-1] = WALL
                            if ([random_wall[0], random_wall[1]-1] not in walls):
                                walls.append([random_wall[0], random_wall[1]-1])

                        if (random_wall[1] != self.width-1): # Check if it is not the rightmost column
                            if (self.maze[random_wall[0]][random_wall[1]+1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]+1] = WALL
                            if ([random_wall[0], random_wall[1]+1] not in walls):
                                walls.append([random_wall[0], random_wall[1]+1])

                    for wall in walls: # deletes wall
                        if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                            walls.remove(wall)

                    continue

            if (random_wall[0] != self.height-1): # bottom wall
                if (self.maze[random_wall[0]+1][random_wall[1]] == UNVISITED and self.maze[random_wall[0]-1][random_wall[1]] == CELL):

                    cells_cache = self.nb_neighbors(random_wall)
                    if (cells_cache < 2):
                        # Denote the new path
                        self.maze[random_wall[0]][random_wall[1]] = CELL

                        # Mark the new walls
                        if (random_wall[0] != self.height-1):
                            if (self.maze[random_wall[0]+1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]+1][random_wall[1]] = WALL
                            if ([random_wall[0]+1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]+1, random_wall[1]])
                        if (random_wall[1] != 0):
                            if (self.maze[random_wall[0]][random_wall[1]-1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]-1] = WALL
                            if ([random_wall[0], random_wall[1]-1] not in walls):
                                walls.append([random_wall[0], random_wall[1]-1])
                        if (random_wall[1] != self.width-1):
                            if (self.maze[random_wall[0]][random_wall[1]+1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]+1] = WALL
                            if ([random_wall[0], random_wall[1]+1] not in walls):
                                walls.append([random_wall[0], random_wall[1]+1])

                    for wall in walls: # deletes the walls
                        if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                            walls.remove(wall)


                    continue
            
            # if it's the leftmost wall
            if (random_wall[1] != self.width-1):
                if (self.maze[random_wall[0]][random_wall[1]+1] == UNVISITED and self.maze[random_wall[0]][random_wall[1]-1] == CELL):

                    cells_cache = self.nb_neighbors(random_wall)
                    if (cells_cache < 2):

                        self.maze[random_wall[0]][random_wall[1]] = CELL

                        if (random_wall[1] != self.width-1):
                            if (self.maze[random_wall[0]][random_wall[1]+1] != CELL):
                                self.maze[random_wall[0]][random_wall[1]+1] = WALL
                            if ([random_wall[0], random_wall[1]+1] not in walls):
                                walls.append([random_wall[0], random_wall[1]+1])
                        if (random_wall[0] != self.height-1):
                            if (self.maze[random_wall[0]+1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]+1][random_wall[1]] = WALL
                            if ([random_wall[0]+1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]+1, random_wall[1]])
                        if (random_wall[0] != 0):	
                            if (self.maze[random_wall[0]-1][random_wall[1]] != CELL):
                                self.maze[random_wall[0]-1][random_wall[1]] = WALL
                            if ([random_wall[0]-1, random_wall[1]] not in walls):
                                walls.append([random_wall[0]-1, random_wall[1]])

                    for wall in walls:
                        if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                            walls.remove(wall)

                    continue

            for wall in walls:
                if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                    walls.remove(wall)
            

        for i in range(0, self.height): # marks the unvisited cells as walls
            for j in range(0, self.width):
                if (self.maze[i][j] == UNVISITED):
                    self.maze[i][j] = WALL

        for i in range(0, self.width): # marks the outer walls
            if (self.maze[1][i] == CELL):
                self.maze[0][i] = CELL
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == CELL):
                self.maze[self.height-1][i] = CELL
                break
    
if __name__ == "__main__":
    maze = Maze(20, 10)
    maze.print_maze()
    for i in range(20):
        print(maze.get_random_cell())

