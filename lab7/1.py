import pygame 
from datetime import datetime

pygame.init()

main_clock = pygame.image.load( "mainclock.png" )
lefthand = pygame.image.load( "leftarm.png" )
righthand = pygame.image.load("rightarm.png")

screen = pygame.display.set_mode(( 900 , 900 ))
clock = pygame.time.Clock()

main_clock_center = main_clock.get_rect( center = (450 , 450) )
lefthand_center = lefthand.get_rect( center = main_clock_center.center )
righthand_center = righthand.get_rect( center = main_clock_center.center )


done = False

while not done :
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True

    current_time = datetime.now().time()

    second_angle = current_time.second*6
    minut_angle = current_time.minute*6

    rotated_right_hand = pygame.transform.rotate(righthand, -minut_angle)
    rotated_left_hand = pygame.transform.rotate(lefthand , -second_angle)

    righthand_center = rotated_right_hand.get_rect( center = main_clock_center.center )
    lefthand_center = rotated_left_hand.get_rect( center = main_clock_center.center )

    screen.blit(main_clock, main_clock_center)  
    screen.blit(rotated_left_hand, lefthand_center) 
    screen.blit(rotated_right_hand, righthand_center) 


    pygame.display.update([ righthand_center, lefthand_center ]) 

    clock.tick(60)



