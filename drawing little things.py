import pygame,sys
from pygame.locals import *
pygame.init()#this flag thing's vital   ________________  right below this line
sur = pygame.display.set_mode((500,400),pygame.DOUBLEBUF)  
pygame.display.set_caption('Let\'s do some drawing.')
BLACK=(0,0,0)
ITE=(128,128,128) #nearly grey
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
orange=(239,98,16) #from net
sur.fill(ITE)
pygame.draw.line(sur,BLUE,(60,60),(120,60),4)
pygame.draw.line(sur,BLUE,(60,120),(120,120),4)
pygame.draw.line(sur,BLUE,(120,60),(60,120))
#pygame.draw.polygon(sur,GREEN, (146,0),(291,106),(236,277),(56,277),(0,106)) --mistaken here.
pygame.draw.polygon(sur, GREEN, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))

#rememebr a thing here .The points are given by a tuple and act as one argument as they are given in a
#''packed tuple''.
pygame.draw.circle(sur,BLUE,(300,50),50,1)
pygame.draw.ellipse(sur,RED,(300,250,40,80),1)
pygame.draw.rect(sur,BLACK,(200,150,100,50),1)
pixObj = pygame.PixelArray(sur)
pixObj[480][380] = orange
pixObj[482][382] = orange
pixObj[484][384] = orange
pixObj[486][386] = orange
pixObj[488][388] = orange
del pixObj
nua=pygame.PixelArray(sur)#i made a method to make a rectangle filled wuth colour
for i in range(100,200):
    for j in range(200,300):
        nua[i][j]= orange
del nua
def mo_rect(origin,xlen,ylen,color):  #now for a rect without color i.e. only bounds
    nua2 = pygame.PixelArray(sur)
    xorigin = origin[0]
    yorigin = origin[1]
    for i in range (xorigin,xorigin+xlen+1):
        nua2[i][yorigin]= color
        nua2[i][yorigin+ylen-1]= color
    for j in range(yorigin,yorigin+ylen):
        nua2[xorigin][j]= color
        nua2[xorigin+xlen][j]= color
    del nua2
mo_rect([10,10],20,20,BLUE)
k=True
while k:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

