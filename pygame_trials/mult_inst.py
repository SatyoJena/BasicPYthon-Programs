import pygame
import sys
from random import randint

pygame.init()
surface = pygame.display.set_mode((1200,750))
pygame.display.set_caption("Multiple rectangles")
VEL = 20
color = (255,0,0)

class Box:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.color = (randint(0,250),randint(0,250),randint(0,250))
	def move(self,dest):
	    if(self.x<dest): #changing just one word, if to while changes a lot of things
	        self.x += randint(5,100)
	        pygame.draw.rect(surface,self.color,(self.x,self.y,10,30))
	        #pygame.time.delay(2)
	        pygame.time.Clock().tick(100)
	        pygame.display.update()
		
instances = [Box(randint(0,20),randint(0,200)) for _ in range(20)]

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #updating instance
    for box in instances:
        box.move(dest = 1100)

