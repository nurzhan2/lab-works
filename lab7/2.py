import pygame 

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode (( 350, 175 ))

done = False

songs = [ "Havana.mp3" , "Do i wanna know .mp3" ]
current_song = 0 

pygame.mixer.music.load( songs[current_song] )
pygame.mixer.music.play()


play = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause() 
                    play = False 
                else :
                    pygame.mixer.music.unpause()
                    play = True 
            if event.key == pygame.K_RIGHT :
                current_song +=1
                if current_song >= len( songs ):
                    current_song = 0
                pygame.mixer.music.load( songs[ current_song ] )
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                current_song -=1
                if current_song < 0 :
                    current_song = len(songs)-1
                pygame.mixer.music.load( songs[ current_song ] )
                pygame.mixer.music.play()
            
            

                    



    

    pygame.draw.rect( screen, (105 , 105 , 105 ), (50 , 35 , 250 , 100) )
    pygame.draw.circle( screen , ( 220 , 220 , 220 ) , (105 , 85) , 40 , 0 )
    pygame.draw.rect( screen , ( 220 , 220 , 220 ) ,( 155 , 80 , 120 , 10) )
    
    font = pygame.font.Font( None , 36)
    text1= font.render( " song # 1 " , True , ( 0 , 0 , 0 ))
    text2= font.render( " song # 2 " , True , ( 0 , 0 , 0 ))

    if current_song == 0 :
        screen.blit( text1 , (155 , 50) )
    else:
        screen.blit( text2 , ( 155 , 50 ) )



    if play :
        pygame.draw.rect ( screen , ( 0 , 0 , 0 ) , ( 90, 65 , 10 , 40 ))
        pygame.draw.rect ( screen , ( 0 , 0 , 0 ) , ( 110, 65 , 10 , 40 ))
    else :
        pygame.draw.polygon ( screen , ( 0 , 0 , 0 ) , ( (92 , 65) , (92, 105) , (130 , 85) ) , 0 )

    pygame.display.flip()




    




