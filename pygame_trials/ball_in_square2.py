# the following program tries to implment a ball in a 3 sided box
# with a broken 4th side where 0 < len(4th side) < len(box)
# Now with collision counts!
# the box is sqaure-like and so is the ball
import pygame
import sys
from math import sqrt, cos, sin, pi

pygame.init()
surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("A Ball in a Square Box")

#colors
RED   = (255,0,0)
GRREN = (0,255,0)
BLUE  = (0,0,255)
CYAN  = (0,255,255)
YELLOW= (255,255,0)
BG_COLOR =(0,0,0)
#constants
FPS = 30
PAUSE = -1 #-1 is play 1 is pause
#may make these global
collision_count =0 #made it global :( in func check_collision_with


#functions
def pause_play():
    PAUSE *= -1


#Classes
class Button:
    def __init__(self,x,y,xl,yl,text = "Text",func = None, bgcolor = RED, textcolor = CYAN, textfont = "timesnewroman"):
        self.x  = x
        self.y  = y
        self.xl = xl
        self.yl = yl
        self.text = text
        self.func = func
        self.bgcolor = bgcolor
        self.textcolor = textcolor
        self.textfont = textfont

        _font = pygame.font.SysFont(self.textfont, int(0.8*self.yl))
        self._text = _font.render(self.text, True, self.textcolor, self.bgcolor)
        self.textRect = (self.x,self.y,self.xl,self.yl)
        surface.blit(self._text, self.textRect)

    def click(self):
        x,y = pygame.mouse.get_pos()
        if ((self.x< x <self.x+self.xl) and (self.y< y <self.y+self.yl)) and (pygame.mouse.get_pressed()[0]) :
            self.func()
class Box:
    def __init__(self,x,y,side,thickness,gap) :
        self.x = x
        self.y = y
        self.side = side
        self.thickness = thickness
        self.gap = gap # 0 < gap < side and always occurs at right 

    def draw (self):
        pygame.draw.rect(surface,BLUE,(self.x,self.y,self.side,self.side),self.thickness)
        # clearing the part of  top to look like a broken box
        pygame.draw.line(surface,BG_COLOR,(self.x+self.side-self.gap,self.y), (self.x+self.side,self.y), self.thickness*2)

        
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

        top = (self.y <= BoxObject.y) and (
        BoxObject.x+BoxObject.thickness<self.x<BoxObject.x+BoxObject.side-BoxObject.gap)

        top_right = (self.x<= BoxObject.x+BoxObject.side-BoxObject.gap) and (self.y<BoxObject.y)
        
        bottom = (self.y+self.side >= BoxObject.y+BoxObject.side-BoxObject.thickness) and (
        BoxObject.x+BoxObject.thickness<= self.x <=BoxObject.x+BoxObject.side-BoxObject.thickness)

        
        global collision_count
        if (left_wall or right_wall or top_right): self.velx*=(-1);collision_count +=1
        elif (top or bottom): self.vely*= (-1); collision_count += 1

    def move(self):
        pygame.draw.rect(surface,RED,(self.x,self.y,self.side,self.side))
        self.x += self.velx
        self.y += self.vely
        
#intialisations
ball  = Ball(250,250,5,7,pi/15)
box   = Box(190,200,200,6,gap=30)
clock = pygame.time.Clock()   
counter = Button  
pause_play_button = Button

#game loop   
while True:

    #quitter code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
    if (PAUSE == -1):
        #surface.fill(BG_COLOR)
        for i in range(box.y,box.y+box.side,10):
            pygame.draw.line(surface,CYAN,(box.x-10,i),(box.x,i),1)
        box.draw()        
        ball.move()
        ball.check_collision_with(box)
        counter(200,100,70,30,f"{collision_count} collisions")
    elif(PAUSE == 1):
        pass
        
    pause_play_button(50,440,50,30,"pause/play",pause_play)
    
    clock.tick(FPS)
    pygame.display.update()
