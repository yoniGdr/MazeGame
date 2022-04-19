import unittest

import sys
sys.path.append('../src/maze')
sys.path.append('../src')

from maze import Maze



class MazeTest(unittest.TestCase):

    def setUp(self):
        self.maze = Maze(10, 10)
        self.start = self.maze.get_start()
        self.end = self.maze.get_end()
        self.width = self.maze.get_width()
        self.height = self.maze.get_height()
  
    def test_maze_init(self):
        self.assertEqual(self.maze.width, 10)
        self.assertEqual(self.maze.height, 10)

    def test_maze_init_with_wrong_size(self):
        with self.assertRaises(Exception):
            Maze(0, 0)


    def test_maze_init_with_wrong_size_2(self):
        with self.assertRaises(Exception):
            Maze(-1, -1)

    def test_maze_has_wall(self):
        # -1 for the start
        for x in range(self.width):
            if(x == self.end[1] or x == self.start[1]): #if start or end
                continue
            self.assertTrue(self.maze.is_wall(0,x))
            self.assertTrue(self.maze.is_wall(self.height-1,x))

        for y in range(self.height):
            self.assertTrue(self.maze.is_wall(y,0))
            self.assertTrue(self.maze.is_wall(y,self.width-1))


    def test_maze_has_start(self):
       
        # the start is not a wall
        self.assertFalse(self.maze.is_wall(self.start[0],self.start[1]))

        # the start is always in the first row
        
        i=0
        for x in range(self.width):
            if not (self.maze.is_wall(0,x)):
                break
            i+=1
        self.assertTrue(i<self.width) 


           
        
        

if __name__ == '__main__':

    unittest.main()
    pygame.quit()

