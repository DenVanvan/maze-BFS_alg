
import os
from time import sleep
from collections import deque

class Maze:

# transforms .txt to list of lists
    def __init__(self, file_path):

        with open(file_path, 'r') as file:
            self.content_initial = file.read().split('\n')
            self.content_processed = [item for item in self.content_initial]
            self.content_processed = [[fig for fig in item] for item in self.content_processed]


# calculates the shortest path out of total path
    def find_path(self, path_dict, point, start_point, path):
        path = [point]

        while point != start_point:
            point = path_dict[point]
            path.append(point)
        return path

# defines if the point is not outside the maze
    def not_Valid(self, point):
        if point[0]<0 or point[0] > len(self.content_processed):
            return True
        elif point[1]<0 or point[1]>len(self.content_processed[0]):
            return True
        else:
            return False

# defines if the point will not hit the wall
    def wall(self, point):
        if self.content_processed[point[0]][point[1]] == '0':
            return True
        else:
            return False

# main function: calculates the shortest path from I to Exit
    def calculate(self):
        visited = []
        Queue = deque()
        start_point = Maze.starting_point(self,'I')
        Queue.appendleft(start_point)
        path_dict = dict()
        final_path = []

        while Queue:

            cur_point = Queue.popleft()

            # moving the grid
            next_points = [(cur_point[0]-1, cur_point[1]), (cur_point[0]+1, cur_point[1]), 
            (cur_point[0], cur_point[1]+1), (cur_point[0], cur_point[1]-1)]

            # checking possible points
            for point in next_points:
                if Maze.not_Valid(self, point):
                    continue
                elif Maze.wall(self, point):
                    continue
                elif point in visited:
                    continue
                elif self.content_processed[point[0]][point[1]] == 'E':
                    path_dict[point] = cur_point
                    print('Solution found: ')
                    return Maze.find_path(self, path_dict,point, start_point, final_path)
                    
                # adding point to queue if valid, not wall, not visited and not exit    
                else:
                    Queue.append(point)
                    path_dict[point] = cur_point

            visited.append(cur_point)


# returns tuple: coordinates for the starting point
    def starting_point(self, starting_point_str):
            for i , row in enumerate(self.content_processed):
                if starting_point_str in row:

                    path = (i,row.index(starting_point_str))
                    return path

# draws the output txt file   
    def draw_maze(self, path):

        content_copy = self.content_processed[:]

        for item in path[1:-1]:
            content_copy[item[0]][item[1]] = '@'

        with open('Maze_out.txt', 'w') as file:
            for row in content_copy:
                for item in row:
                    file.write(item)
                file.write('\n')

        


            




