import pygame
import sys
from tkinter import messagebox, Tk



window_width = 1000
window_height = 500

# initializing display of required width and height 
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('pathfinding visualization')


coloumn = 50
row = 25

box_width = window_width // coloumn
box_height = window_height // row

grid = []

class Box:
    def __init__(self ,i,j):   # init used as constructor self used as instance i and j is row and coloumn
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
    # draw used to draw little boxes in canvas 
    def draw(self, win , color):
        pygame.draw.rect(win,color,(self.x*box_width, self.y*box_height, box_width-2, box_height-2))

#create grid 
for i in range(coloumn):
    arr = []
    for j in range(row):
        arr.append(Box(i,j))
    grid.append(arr)

start_box = grid[0][0]
start_box.start = True

    

def main():
    begin_search = False
    target_box_set = False
    while True:
        for event in pygame.event.get():
            #quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # mouse control for getting position of walls while creating with the help of mouse
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]   #  this function return tuple so we can take as a seperate window
                y = pygame.mouse.get_pos()[1]
                # draw wall
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True
                #set target wall or block
                if event.buttons[2] and not target_box_set:
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
           # start algorithm 
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
               
            
            
                
            
        window.fill((0,0,0))
        
        for i in range(coloumn):
            for j in range(row):
                box = grid[i][j]
                box.draw(window, (50,50,50))
                if box.start:
                    box.draw(window,(0,200,200))
                if box.wall:
                    box.draw(window,(90,90,90))
                if box.target:
                    box.draw(window,(200,200,0))
        
        pygame.display.flip()


main()