import pygame

window_width = 500
window_height = 500

coloumn = 25
row = 25

box_width = window_width // coloumn
box_height = window_height // row
class Box:
    def __init__(self ,i,j):   # init used as constructor self used as instance i and j is row and coloumn
        self.x = i
        self.y = j
    # draw used to draw little boxes in canvas 
    def draw(self, win , color):
        pygame.draw.rect(win,color,(self.x*box_width, self.y*box_height, box_width-2, box_height-2))
