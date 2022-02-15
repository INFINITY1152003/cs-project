
import random
import math
import pygame
from pygame import mixer#mixer is a class which help is to handle all kind of music in our game

           #initialise pygame
pygame.init()

           #creating screen
screen=pygame.display.set_mode((800,600))


         #loding background image
background = pygame.image.load(('img1/background.png'))

            #background sound

mixer.music.load('img1/m.wav')#to add "music" to the background  of the game      
mixer.music.play(-1)#-1 is added so it can be played in loop

             #title and caption
pygame.display.set_caption('WAR SHIP')
icon=pygame.image.load('img1/space-ship.png')
pygame.display.set_icon(icon)


                  #player
playerImg=pygame.image.load('img1/ufo.png ')
playerx=370
playery=480
playerx_change=0

                  #enemy
enemyImg=[]   
enemyx=[]
enemyy= []
enemyx_change=[]
enemyy_change=  []   
num_of_enemies = 6

for i in range(num_of_enemies):        
    enemyImg.append(pygame.image.load('img1/aircraft.png '))
    enemyx.append(random.randint(0,735))#the camond random.randint allows to chose any int. value between start value and end value
    enemyy.append(random.randint(50,150))
    enemyx_change.append(2)
    enemyy_change.append(40)



                     #bullet
bulletImg=pygame.image.load('img1/bullet.png ')
bulletx=0
bullety=480
bulletx_change=0
bullety_change=6
bullet_state = "ready"#ready is you can't see the bullet on the screen
                      #fire the bullet is in motion meaning moving
                        

                        # score
                        


score_value=0
font=pygame.font.Font('freesansbold.ttf' , 32)#to add text we ne use  pygame.font.Font('name of the font',size)
textx=10#giving axis                               
texty=10

                   #GAME OVER TEXT
                   
over_font=pygame.font.Font('freesansbold.ttf' , 64)    


             
def show_score(x,y):
    score=font.render("SCORE :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
    
    
def game_over_text(x,y): 
    over_text=over_font.render("GAME OVER",True,(255,0,0))
    screen.blit(over_text,(200,250))
    
    
    
def player(x,y):
    screen.blit(playerImg,(x,y))  #blit is the method to call image
    
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
    
def fir_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
    
def isCollison(enemyx,enemyy,bulletx,bullety):  
    distance = math.sqrt(math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2))
    if distance<27:
        return True
    else:
        return False
         #GAME LOOP
run=True 
while run:
           
#RGB-RED,GREEN,BLUE BY USING IT WE CAN IMPLIMENT ANY COLOURE ON TH SCREEN THE MAXIMUM CONSETRION OF COLOURE IS 255 NOT MORE THAN THAT
    screen.fill((0,0,0))
    
    
                               #background image
    screen.blit(background,(0,0))
    
    
    #event handlaer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            #if key is pressed check weather its right or left

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_UP:    #it first checks that th bullet is on the screen or not
            
                if bullet_state is "ready": #if it is not on screen then it makes shure that it can get current x cordinate of spaceship & 
                    bullet_Sound = mixer.Sound('img1/laser.wav')
                    bullet_Sound.play()
                    bulletx=playerx         #stores in variable bulletx
                    fir_bullet(playerx,bullety)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_change = 0
            if event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerx+=playerx_change
    
    
    #creating boundaries so the ship does not go out of the game window
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:#your game window size is 800 pixal and spaceship size is 64 pixal so 800-64=736    
        playerx = 736
            
    
    
    
                      #movement of enemy
    for i in range(num_of_enemies):     

                    #GAME OVER
        if enemyy[i]>440:                
        
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text(440,2000)
            break
        enemyx[i]+=enemyx_change[i]    
        #creating boundaries so the ship does not go out of the game window
   
        if enemyx[i] <= 0:
            enemyx_change[i] = 3
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i] >= 736:#your game window size is 800 pixal and spaceship size is 64 pixal so 800-64=736    
            enemyx_change[i] = -3
            enemyy[i]+=enemyy_change[i]
            
            
            
                          #COLLISON
        collosion=isCollison(enemyx[i],enemyy[i],bulletx,bullety)    
        if collosion:
            explision_Sound = mixer.Sound('img1/e.wav')
            explision_Sound.play()
            bullety=480
            bullet_state="ready"
            score_value+=10
          
            enemyx[i]=random.randint(0,736)#the camond random.randint allows to chose any int. value between start value and end value
            enemyy[i]=random.randint(50,150)        
    
        enemy(enemyx[i],enemyy[i],i)           
                      #bullet movement
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state is "fire":
        fir_bullet(bulletx,bullety)
        bullety-=bullety_change
        
                      
             #you need to update your window so the game window can work 
    player(playerx,playery)        
    show_score(textx,texty) 
    pygame.display.update()