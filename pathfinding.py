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
    # draw used to draw little boxes in canvas 
    def draw(self, win , color):
        pygame.draw.rect(win,color,(self.x*box_width, self.y*box_height, box_width-2, box_height-2))

#create grid 
for i in range(coloumn):
    arr = []
    for j in range(row):
        arr.append(Box(i,j))
    grid.append(arr)
    

def main():
    while True:
        for event in pygame.event.get():
            #quit window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        window.fill((0,0,0))
        
        for i in range(coloumn):
            for j in range(row):
                box = grid[i][j]
                box.draw(window, (50,50,50))
        
        pygame.display.flip()


main()