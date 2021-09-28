
import os
from time import sleep
class Maze:

    def __init__(self, file_path):

        with open(file_path, 'r') as file:
            self.content_initial = file.read().split('\n')
            self.content_processed = [item.replace(' ', '1') for item in self.content_initial]
            self.content_processed = [[fig for fig in item] for item in self.content_processed]


    def draw_maze(self, path):

        self.draw = ''
        os.system('cls')

        content_copy = self.content_processed[:]

        for item in path:
            content_copy[item[0]][item[1]] = '.'
        content_copy[path[-1][0]][path[-1][1]]= 'M'

        for row in content_copy:
            for item in row:
                self.draw += item.replace('0','█').replace('1',' ')
            self.draw += '\n'
        print(self.draw)

    def move(self, path):
        sleep(1)
    
        cur_pos = path[-1]
        Maze.draw_maze(self, path)
        possibles = ((cur_pos[0],cur_pos[1]+1), (cur_pos[0], cur_pos[1]-1), (cur_pos[0]+1,cur_pos[1]), 
        (cur_pos[0]-1, cur_pos[1]))
        
        for item in possibles:
            if item[0]<0 or item[1]<0 or item[0]>len(self.content_processed) or item[1]>len(self.content_processed[0]):
                continue
            elif item in path:
                continue
            elif self.content_processed[item[0]][item[1]] == '0':
                continue
            elif self.content_processed[item[0]][item[1]] == 'E':
                path += (item,)
                print('Found!')
            else:
                newpath = path + (item,)
                Maze.move(self, newpath)




    def starting_point(self, starting_point_str):
            for i , row in enumerate(self.content_processed):
                if starting_point_str in row:

                    path = ((i,row.index(starting_point_str)),)
                    return(path)

        


            




