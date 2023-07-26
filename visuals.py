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
queue = []
path = []

class Box:
    def __init__(self ,i,j):   # init used as constructor self used as instance i and j is row and coloumn
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None
        
    # draw used to draw little boxes in canvas 
    def draw(self, win , color):
        pygame.draw.rect(win,color,(self.x*box_width, self.y*box_height, box_width-2, box_height-2))
    
    def set_neighbours(self):
        # horizontal neighbours 
        if self.x > 0:
            self.neighbours.append(grid[self.x-1][self.y])
        if self.x < coloumn-1:
            self.neighbours.append(grid[self.x+1][self.y])
        # vertical neighbours 
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y-1])
        if self.y < row-1:
            self.neighbours.append(grid[self.x][self.y+1])
        # diagnol distance 
        if self.x >0 and self.y >0:
            self.neighbours.append(grid[self.x-1][self.y-1])
        if self.x <coloumn-1 and self.y>0:
            self.neighbours.append(grid[self.x+1][self.y-1])
        if self.x<coloumn-1 and self.y<row-1:
            self.neighbours.append(grid[self.x+1][self.y+1])
        if self.x>0 and self.y<row-1:
            self.neighbours.append(grid[self.x-1][self.y+1])
        
            
            
#create grid 
for i in range(coloumn):
    arr = []
    for j in range(row):
        arr.append(Box(i,j))
    grid.append(arr)

# set neighbours
for i in range(coloumn):
    for j in range(row):
        grid[i][j].set_neighbours()

# start_box = grid[0][0]
# start_box.start = True
# start_box.visited = True
# queue.append(start_box)



def main():
    begin_search = False
    target_box_set = False
    searching = True         #it become false once we found the target and it stops the searching  
    target_box = None  # store the box we wanted to reach 
    start_box_set = False
    
    while True:
        for event in pygame.event.get():
            #quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    x, y = pygame.mouse.get_pos()
                    i = x // box_width
                    j = y // box_height
                    if not start_box_set and not grid[i][j].wall:
                       start_box = grid[i][j]
                       start_box.start = True
                       start_box.visited = True
                       start_box_set = True
                       queue.append(start_box)
                       
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
        
        if begin_search:
            if len(queue)>0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box 
                            queue.append(neighbour)
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("no solution, there is not path")
                    searching = False
                
            
               
            
            
                
            
        window.fill((0,0,0))
        
        for i in range(coloumn):
            for j in range(row):
                box = grid[i][j]
                box.draw(window, (50,50,50))
                if box.queued:
                    box.draw(window,(200,0,0))
                if box.visited:
                    box.draw(window,(0, 128, 255))
                if box in path:
                    box.draw(window, (0, 100, 0))
                if box.start:
                    box.draw(window,(0,200,200))
                if box.wall:
                    box.draw(window,(90,90,90))
                if box.target:
                    box.draw(window,(200,200,0))
        
        pygame.display.flip()