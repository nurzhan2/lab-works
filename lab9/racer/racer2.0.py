import pygame, sys
from pygame.locals import *
import random, time 

pygame.init() 
pygame.mixer.init()




screen = pygame.display.set_mode(( 400 , 600 ))
screen.fill(( 255, 255, 255 ))
pygame.display.set_caption( "Game" )


fps = pygame.time.Clock()

w = 1
font_fc = pygame.font.SysFont( "Comic Sans" , 30)


class coins( pygame.sprite.Sprite ):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load( "Coin.png" )
        self.rect = self.image.get_rect()
        

        x = random.randint( 0 , 2 )*104 + 44 + 52
        y = random.randint( 250 , 550 )

        self.rect.center = ( x , y )


    def weight ( self , screen , font , ves):

        w = font.render( str(ves) , True , ( 0,0,0))

        screen.blit( w , (self.rect.left +13 , self.rect.top) )
        



    def draw( self , screen ):
        screen.blit ( self.image , self.rect )



class player( pygame.sprite.Sprite ):
    def __init__(self ):
        super().__init__()
        self.image = pygame.image.load( "Player.png" )
        self.rect = self.image.get_rect()
        self.rect.center = ( 160, 520 ) 

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.top > 5 and keys[ pygame.K_UP] : self.rect.move_ip( 0 , -5 )
        if self.rect.bottom < 600 and keys[ pygame.K_DOWN ]: self.rect.move_ip( 0 , 5 )
        if self.rect.right < 400 and keys[ pygame.K_RIGHT ]: self.rect.move_ip( 5 , 0 )
        if self.rect.left > 5 and keys[ pygame.K_LEFT ]: self.rect.move_ip( -5 , 0 )

    def draw( self , screen ):
        screen.blit( self.image , self.rect )
        



class enemy( pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load( "Enemy.png" )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint( 40 , 360 ) , 0 ) 

    def move(self):



        self.rect.move_ip ( 0 , speed )
        if ( self.rect.bottom > 600 ):
            self.rect.top = 0
            self.rect.center = ( random.randint( 40 , 360 ) , 0 )

    def draw ( self , screen ):
        screen.blit( self.image , self.rect )


        

p = player()
e = enemy()
c = coins()





count_of_coins = 0 

font = pygame.font.SysFont( "Comic Sans" , 60 )
font_small= pygame.font.SysFont( "Comic Sans" , 20 )

g_o = font.render( "Game Over" , True , (0 , 0 , 0) )



bg = pygame.image.load( "bg.png" )

speed = 1


done = False
while not done:
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    score = font_small.render ( str(count_of_coins) , True  , (0,0,0) )
    
    screen.blit( bg, (0,0) )
    if count_of_coins >=5: speed = count_of_coins - count_of_coins%5
    


    p.update()
    e.move()

    c.draw(screen)
    c.weight ( screen , font_fc , w )
    p.draw(screen)
    e.draw(screen)

    



    if c.rect.colliderect( p.rect ):
        count_of_coins +=w
        w = random.randint( 1, 3 )
        pygame.mixer.music.load( "coin.mp3" )
        pygame.mixer.music.play(1)

        
        x = random.randint( 0 , 2 )*104 + 44 + 52
        y = random.randint( 250 , 550 )

        c.rect.center = ( x , y )



    screen.blit( score,( 10 , 10 ) )

    if p.rect.colliderect(e.rect):

        pygame.mixer.music.load( "crash.wav" )
        pygame.mixer.music.play(1)

        time.sleep( 0.5 )

        screen.fill(( 255, 0 , 0 ))
        screen.blit( g_o , ( 30 , 250 ) )
        pygame.display.update()
        

        time.sleep(1.5)
        sys.exit()




    pygame.display.update()
    fps.tick(60) 
    