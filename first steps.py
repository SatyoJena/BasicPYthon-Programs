import pygame
pygame.init()
de = pygame.display.set_mode((600,800))
#de heuchi pgame window or 'surface'.
pygame.display.set_caption('steins;gate')
#jadi gote 2d shape baneibara achi tahele default syntax is as follows:
#draw.[SHAPE](SURFACE,(R,G,B),(X posn,Y posn,X length,Y length))
#as we are going to make a rectangle lets put it all
x_p=50
y_p=50
x_l=40
y_l=60
vel=5#instruction dele jinisha ta kete pixel move kariba
#main loop
run=True
while run:
    pygame.time.delay(30)#milisecond
    #it is done so that things go smooth
    for event in pygame.event.get(): #it is alist of all events occuring due to user.
        if event.type== QUIT:
            run=False
    keys= pygame.key.get_pressed()#list of all key inputs by user
    if keys[pygame.K_LEFT]:       #ei input asile jinishara x y coordinate re changes asiba
        x_p-=vel#velocity ra kama ethe asiba arthat ama rectangle 5 pixels move kariba 0.1 sec re
    if keys[pygame.K_RIGHT]:
        x_p+=vel
    if keys[pygame.K_UP]:
        y_p-=vel
    if keys[pygame.K_DOWN]:
        y_p+=vel
    #ei jagare gadi draw karibu,old rct guda livibani.actually tu move karunu nua posn set kari
    #nua rect banauchu ta old rect ku livaiba ta mu janini kinti ta upare blck color chadheidele
    #kaam khalas---syntax hela "[SURFACE].fill((R,G,B))" black pain RGB 000 heijiba
    de.fill((0,0,0))
    pygame.draw.rect(de,(200,0,0),(x_p,y_p,x_l,y_l)
    #pygame.display.update()
    #initialise karichu mane 'quit' bi karibu.
    #this pon re quit kale kichi display habani.
    #sethipain surface ku refresh karibakunpade.so we do as follws
    
    #ebe khali display haba input naba pain draw kariba purbaru input instructions debu.
    #ebe sesa heba
pygame.quit()


    
