import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1300, 750))
pygame.display.set_caption('Hello World!')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
fontObj = pygame.font.SysFont('papyrus',50)
textSurfaceObj = fontObj.render('abcdefghijklmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyz', True, GREEN)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (650, 150)
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

#conclusion use SysFont.
#papyrus gigi inkfree are to be used as they are good.
#on nearly fullscreening 52 characters can be accomadated comfortably.
