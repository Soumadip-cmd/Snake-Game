import pygame
import time
import random
pygame.init()

win=pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Game')

red=(255,0,0);green=(0,255,0);blue=(0,0,255);white=(255,255,255);black=(0,0,0,);cyan=(0,255,255);orange=(232,103,8);brown=(59,26,2)
violet=(86,9,168);yellow=(173,156,11)

#massage function
smallfonts=pygame.font.SysFont("Footlight MT Light",40)
medfonts=pygame.font.SysFont("Harrington",50)
largefonts=pygame.font.SysFont("Lucida Handwriting",65)

def textobj(text,clr,size):
    if size=='small':
        textsurf=smallfonts.render(text,True,clr)
    elif size=='med':
        textsurf=medfonts.render(text,True,clr)
    elif size=='large':
        textsurf=largefonts.render(text,True,clr)
    return textsurf,textsurf.get_rect()

def message_text(masg,clr,position,size):
    textsurf,textrect=textobj(masg,clr,size)
    textrect.center=(400),(300)+position
    win.blit(textsurf,textrect)
    pygame.display.update()
def snake(blocksize,snakelist):
    for xny in snakelist:
        pygame.draw.rect(win,black,[xny[0],xny[1],blocksize,blocksize])
def gameintro():
    win.fill(yellow)
    message_text('Start Game',red,-100,'large')
    message_text('You have to eat more apple as you can',black,20,'small')
    message_text('.. > P=Paused < ..',black,60,'small')
    message_text('Pls wait for 5 Sec..',violet,200,'small')
    pygame.display.update()
    time.sleep(5)

def score(score):
    text=smallfonts.render("Score:"+str(score),True,black)
    win.blit(text,(0,0))
        
    
def pause():
    win.fill(orange)
    message_text('Paused',blue,20,'large')
    message_text('..Press C to play again and Q to quit..',violet,100,'small')
    
    paused=True
    run=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                paused=False
            elif event.key==pygame.K_q:
                pygame.quit()
                
    
        pygame.display.update()
        
        
def gameover():
    win.fill(white)
    message_text('Game Over',red,-50,'large')
    message_text('Press c to play again and q to quit',red,50,'med')
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    
                    pygame.quit()
                elif event.key==pygame.K_c:
                    gameloop()
                
    pygame.display.update()
    
def gameloop():
    x=400
    y=300
    change_x=0
    change_y=0
    vel=10 
    snakelist=[]
    snakelength=1
    randappleX=round(random.randrange(0,(800-20))/10.0)*10.0
    randappleY=round(random.randrange(0,(600-20))/10.0)*10.0
    
    run=True
    
    while run:
    
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            change_x=-vel
            change_y=0
        if keys[pygame.K_RIGHT]:
            change_x=+vel
            change_y=0
        if keys[pygame.K_UP]:
            change_y=-vel
            change_x=0
        if keys[pygame.K_DOWN]:
            change_y=+vel
            change_x=0
        if keys[pygame.K_p]:
            pause()

        if x>=800 or x<0 or y>=600 or y<0:
            gameover()
            
        x+=change_x
        y+=change_y
        
        
        
        
        win.fill(white)
        pygame.draw.rect(win,red,[randappleX,randappleY,20,20])
        # below 7 line is denote the snake length:
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        snake(20,snakelist)
        
        
        # this is say  if i eat random apple my length id added 
        if x==randappleX and y==randappleY:
            randappleX=round(random.randrange(0,(800-20))/10.0)*10.0
            randappleY=round(random.randrange(0,(600-20))/10.0)*10.0
            snakelength+=1
            
        score(snakelength-1)
        pygame.display.update()
        
    pygame.quit()

gameintro()
gameloop()
