import pygame
pygame.init()

screen = pygame.display.set_mode(( 600 , 600 ))
clock = pygame.time.Clock()
radius = 25

x = 0
y = 0

done = False




while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    screen.fill((255 , 255 , 255))

    keys = pygame.key.get_pressed()

    if keys[ pygame.K_LEFT ] and x - radius > 0:
        x-=20
    if keys[ pygame.K_RIGHT ] and x + radius < 600 :
        x+=20
    if keys[ pygame.K_UP ] and y - radius > 0 :
        y-=20
    if keys[ pygame.K_DOWN ] and y + radius < 600 :
        y+=20

    circle = pygame.draw.circle( screen, (255 , 0 , 0 ) , (x, y) , radius , 0 )

    

    

    clock.tick(60)
    pygame.display.flip()
    
    

