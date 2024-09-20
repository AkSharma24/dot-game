import pygame
import random
import sys
pygame.init()#initialize the pygame
window_size=(400,400)#tuple for size of window
screen=pygame.display.set_mode(window_size)#itset the size
pygame.display.set_caption('white-dot')#it set the title
screen.fill((100,0,0))#it is for color
pygame.draw.circle(screen,(255,255,255),(window_size[0]//2,window_size[1]//2),3) # it draws the circle, at center (window,color,pos[0],pos[1],radius)
x=window_size[0]//2#it stores the post of ball x-axis
y=window_size[1]//2#for y-axis
EnemyX=random.randint(0,397)
EnemyY=random.randint(0,397)
Enemy2X=random.randint(0,397)
Enemy2Y=random.randint(0,397)
print(EnemyX,EnemyY,Enemy2X,Enemy2Y)
speed=2# it stores speed of ball
x_speed=2
y_speed=2
speed_L=2
speed_R=2
speed_U=2
speed_D=2
import random 
xP=random.randint(0,397)
yP=random.randint(0,397)
score=0
scorefont=pygame.font.Font(None,36)# itcreates scorefont
scoreFin=pygame.font.Font(None,56)
speedEnemy=5
def movement():
    global speedEnemy,EnemyX,EnemyY
    
    distEnemy=0
    want = random.randint(0,1)
    if want == 0:
        if EnemyY<0:
            speedEnemy=-speedEnemy
            EnemyY=0

        elif EnemyY>window_size[1]-3:
            speedEnemy=-speedEnemy
            EnemyY=window_size[1]-3
        else:
            EnemyY+=speedEnemy
    if want == 1:
        if EnemyX>window_size[0]-3:
            speedEnemy=-speedEnemy
            EnemyX=window_size[0]-3
        elif EnemyX<0:
            speedEnemy=-speedEnemy
            EnemyX=0
        else:
            EnemyX+=speedEnemy
    distEnemy=((x-EnemyX)**2+(y-EnemyY)**2)**0.5

    if distEnemy<=8:
        score_text=scoreFin.render('SCORE:'+str(score)+'Press any key to quit',True,(0,0,255))
        screen.blit(score_text,(100,200))
        pygame.display.flip()
        pygame.event.wait(4000)
        pygame.quit()
        sys.exit
        
        print('lost')
p=3
def movement2():
    global speedEnemy,Enemy2X,Enemy2Y
    
    distEnemy=0
    want = random.randint(0,1)
    if want == 0:
        if Enemy2Y<0:
            speedEnemy=-speedEnemy
            Enemy2Y=0

        elif Enemy2Y>window_size[1]-3:
            speedEnemy=-speedEnemy
            Enemy2Y=window_size[1]-3
        else:
            Enemy2Y+=speedEnemy
    if want == 1:
        if Enemy2X>window_size[0]-3:
            speedEnemy=-speedEnemy
            Enemy2X=window_size[0]-3
        elif Enemy2X<0:
            speedEnemy=-speedEnemy
            Enemy2X=0
        else:
            Enemy2X+=speedEnemy
    distEnemy=((x-Enemy2X)**2+(y-Enemy2Y)**2)**0.5

    if distEnemy<=8:
        
        score_text=scoreFin.render('SCORE:'+str(score),True,(0,0,255))
        screen.blit(score_text,(100,200))
        pygame.display.flip()
        pygame.time.wait(4000)
        pygame.quit()
        sys.exit
        print('lost')
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    
    movement()
    movement2()
    

    if keys[pygame.K_UP]:
        y-=speed_U
        if y-3<0:
            y=3
    elif keys[pygame.K_DOWN]:
        y+=speed_D
        if y+3>window_size[0]:
            y=window_size[1]-3
        
    elif keys[pygame.K_LEFT]:
        x-=speed_L
        if x-3<0:
            x=3#it set the x value to 3 because after this when update it remains there
        
    elif keys[pygame.K_RIGHT]:
        x+=speed_R
        if x+3>window_size[0]:
            x=window_size[0]-3
    distance=((x-xP)**2+(y-yP)**2)**0.5
    
    if distance<=8:
        xP=random.randint(0,397)
        yP=random.randint(0,397)
        score+=1
        p+=1
        print('won')
    dir=random.randint(0,3)
    
    screen.fill((0,0,0))
   
        
    pygame.draw.circle(screen,(0,255,0),(Enemy2X,Enemy2Y),5)
    pygame.draw.circle(screen,(0,255,0),(EnemyX,EnemyY),5)

    pygame.draw.circle(screen,(215,125,125),(xP,yP),5)
    
    pygame.draw.circle(screen,(255,255,255),(x,y),p)
    
    score_text=scorefont.render('SCORE:'+str(score),True,(255,255,255))
    screen.blit(score_text,(10,10))
    pygame.display.flip()#it basically updates
    pygame.time.Clock().tick(60)