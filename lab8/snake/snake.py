
import pygame, random , time , sys 

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

theme_music = pygame.mixer.Sound( "music.mp3" )
theme_music.play()

grid_size = 50
background = pygame.image.load("bg.jpg")
screen.blit(background, (0, 0))

current_pos = [[350, 300]]
direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT])

grape_count = 0

    
grape_x = random.randint( 0 , 13 )*50
grape_y = random.randint( 0 , 11 )*50

walls = []
food_score = 0 
font = pygame.font.SysFont( "Comic Sans" , 100 )
game_over = font.render( "GAME OVER" , True , ( 0,0,0 ) )

font_small = pygame.font.SysFont( "Comic Sans" , 20 )
font_mid = pygame.font.SysFont( "Comic Sans" , 30 )


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:

            pygame.mixer.music.load( "move.mp3" )
            pygame.mixer.music.play(1)

            if event.key == pygame.K_DOWN and direction != pygame.K_UP:
                direction = pygame.K_DOWN
            if event.key == pygame.K_UP and direction != pygame.K_DOWN:
                direction = pygame.K_UP
            if event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                direction = pygame.K_LEFT
            if event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                direction = pygame.K_RIGHT


    




    new = current_pos.copy()
    
    if direction == pygame.K_DOWN:
        new[0][1] += grid_size
        if new[0][1] >= 600 :
            new[0][1] = 0 

    if direction == pygame.K_UP:
        new[0][1] -= grid_size
        if new[0][1] < 0 :
            new[0][1] = 550

    if direction == pygame.K_LEFT:
        new[0][0] -= grid_size
        if new[0][0] < 0 :
            new[0][0] = 650

    if direction == pygame.K_RIGHT:
        new[0][0] += grid_size
        if new[0][0] >= 700:
            new[0][0] = 0

    current_pos.insert(0, [new[0][0], new[0][1]]) 
    current_pos.pop()

          




    screen.blit(background, (0, 0))

    pygame.draw.rect( screen , (134,115,161) , ( grape_x , grape_y , 50 , 50 ) )
    pygame.draw.rect( screen , (115,81,132) , ( grape_x , grape_y , 50 , 50 ) , 5 )     
    
    if current_pos[0][0] == grape_x and current_pos[0][1] == grape_y:
        food_score +=1
        pygame.mixer.music.load("food.mp3")
        
        pygame.mixer.music.play(1)

        wall_x = random.randint( 0 , 13 ) * 50
        wall_y = random.randint( 0 , 11 ) * 50

        while [wall_x , wall_y] in current_pos:

            wall_x = random.randint( 0 , 13 ) * 50
            wall_y = random.randint( 0 , 11 ) * 50

        walls.append( [wall_x , wall_y] )


        current_pos.insert(0 , ([ grape_x , grape_y ]))

        while [ grape_x , grape_y ] in current_pos or [ grape_x , grape_y ] in walls :

        

            grape_x = random.randint( 0 , 13 )*50
            grape_y = random.randint( 0 , 11 )*50
    
    
    score = font_small.render ( ("Score : " + str (food_score)) , True, (255,215,0 )  )
    screen.blit( score , (3 , 3) )

    for i in current_pos:
        pygame.draw.rect (screen, ( 0,153,0), (i[0], i[1], grid_size, grid_size) )
        pygame.draw.rect(screen, ( 40,114,51), (i[0], i[1], grid_size, grid_size) , 5)

    for i in walls :
        pygame.draw.rect( screen, ( 205,92,92 ) , ( i[0] , i[1] , 50 , 50 ) )
        pygame.draw.rect( screen, ( 162,35,29 ) , ( i[0] , i[1] , 50 , 50 ) , 5 )
        
    if current_pos[0] in walls:

        

        theme_music.stop()
        pygame.mixer.music.load("gameover.mp3")
        pygame.mixer.music.play(1)
        
        screen.fill( (10,95,56) )
        Total = font_mid.render( ("TOTAL SCORE : " + str( food_score )) , True , (255,215,0) )
        screen.blit( Total , ( 200 , 300 ) )
        screen.blit( game_over , ( 50 , 150 ) )

        pygame.display.update()
        time.sleep (2)
        sys.exit() 

    


    pygame.display.update()
    clock.tick(4)

pygame.quit()
