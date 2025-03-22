import pygame , random
from collections import deque
pygame.init()

running = True




color_mode = random.choice([ "blue" , "red" , "green" , "white"])
radius = 40
points = deque(maxlen=256)

screen = pygame.display.set_mode(( 600 , 600 ))
clock = pygame.time.Clock()
screen.fill(( 255, 255, 255 ))


def draw( color_mode , index , start , end , radius ):
        
        if color_mode == "blue":
            gradient_color = ( index , index , 255 )
        elif color_mode == "red":
            gradient_color = ( 255 , index , index )
        elif color_mode == "green": 
            gradient_color = (index , 255 , index )
        elif color_mode == "white" :
            gradient_color = ( 255 , 255 , 255 )


        delta_x = ( start[0]-end[0] )
        delta_y = ( start[1]-end[1] )

        iterations = max( abs( delta_x) , abs( delta_y ) )


        for i in range( iterations ):
            progress = i/iterations
            aprogress = 1 - progress

            x = int ( aprogress * start[0] + progress*end[0] )
            y = int ( aprogress * start[1] + progress*end[1] )

            pygame.draw.circle( screen , gradient_color , (x , y) , radius )
            



while running :

    screen.fill((255 , 255 , 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False 

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r  :
                color_mode = "red"
                
            if event.key == pygame.K_g  :
                color_mode = "green"
                
            if event.key == pygame.K_b :
                color_mode = "blue"

            if event.key == pygame.K_e :
                color_mode = "white"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 : radius -=1 
            elif event.button == 3 : radius +=1

        if event.type == pygame.MOUSEMOTION:

            position = event.pos
            points.append( position )

            



    i = 0   
    while i != len(points) - 1:

        draw ( color_mode , i , points[i] , points[i+1] ,radius )

        i +=1

    
    









    pygame.display.update()
    clock.tick(60)


pygame.quit()    