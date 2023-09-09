# the following program tries to implment a ball in a 3 sided box
# the box is sqaure-like and so is the ball
import pygame
import sys
from math import sqrt, cos, sin, pi

surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("A Ball in a Square Box")

#colors
RED   = (255,0,0)
GRREN = (0,255,0)
BLUE  = (0,0,255)
CYAN  = (0,125,125)
BG_COLOR =(0,0,0)


#may make these global
collision_count =0 #made it global :( in func check_collision_with

class Box:
    def __init__(self,x,y,side,thickness) :
        self.x = x
        self.y = y
        self.side = side
        self.thickness = thickness

    def draw (self):
        pygame.draw.rect(surface,BLUE,(self.x,self.y,self.side,self.side),
        self.thickness)
        # clearing the top to look like 3 sided box
        pygame.draw.line(surface,BG_COLOR,
        (self.x,self.y), (self.x+self.side,self.y), self.thickness*2)

        
class Ball:
    def __init__(self,x,y,side,vel,theta): # theta w.r.t X-axis
        self.x = x
        self.y = y
        self.side = side
        self.vel = vel
        self.theta = theta
        self.velx = int(vel*cos(theta))
        self.vely = int(vel*sin(theta))

    def check_collision_with(self,BoxObject):
        left_wall  = (self.x <= BoxObject.x+BoxObject.thickness) and (
        BoxObject.y<= self.y <=BoxObject.y+BoxObject.side)
        
        right_wall = (self.x+self.side >= BoxObject.x+BoxObject.side-BoxObject.thickness) and (
        BoxObject.y<= self.y <=BoxObject.y+BoxObject.side)
        
        bottom = self.y+self.side >= BoxObject.y+BoxObject.side-BoxObject.thickness and (
        BoxObject.x<= self.x <=BoxObject.x+BoxObject.side)

        global collision_count
        if (left_wall or right_wall): self.velx*=(-1);collision_count +=1
        elif bottom : self.vely*= (-1); collision_count += 1

    def move(self):
        pygame.draw.rect(surface,RED,(self.x,self.y,self.side,self.side))
        self.x += self.velx
        self.y += self.vely
        
#intialisations
ball  = Ball(200,200,5,7,pi/20)
box   = Box(190,200,200,6)
clock = pygame.time.Clock()     


   
while True:

    #quitter code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nno. of collision =",collision_count)
            pygame.quit()
            sys.exit()
            
    
    surface.fill(BG_COLOR)
    box.draw()        
    ball.move()
    ball.check_collision_with(box)
    clock.tick(60)
    pygame.display.update()
