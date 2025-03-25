import pygame
import random
import time
import sys

# Initialize 
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
grid_size = 50
FPS = 4

# Colors
GREEN = (0, 153, 0)
DARK_GREEN = (40, 114, 51)
RED = (205, 92, 92)
DARK_RED = (162, 35, 29)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Load 
background = pygame.image.load("bg.jpg")
theme_music = pygame.mixer.Sound("music.mp3")


#time

end = time.time()+5


def play_music(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(1)

def draw_text(text, font_size, color, position):
    font = pygame.font.SysFont("Comic Sans", font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def generate_random_position():
    return random.randint(0, 13) * grid_size, random.randint(0, 11) * grid_size

# Game Variables
theme_music.play()
current_pos = [[350, 300]]
direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT])
food_score = 0
grape_x, grape_y = generate_random_position()
walls = []
weight = random.randint(1, 3)

def update_snake_position():
    new_pos = current_pos.copy()
    
    if direction == pygame.K_DOWN:
        new_pos[0][1] += grid_size
        if new_pos[0][1] >= SCREEN_HEIGHT:
            new_pos[0][1] = 0
    elif direction == pygame.K_UP:
        new_pos[0][1] -= grid_size
        if new_pos[0][1] < 0:
            new_pos[0][1] = SCREEN_HEIGHT - grid_size
    elif direction == pygame.K_LEFT:
        new_pos[0][0] -= grid_size
        if new_pos[0][0] < 0:
            new_pos[0][0] = SCREEN_WIDTH - grid_size
    elif direction == pygame.K_RIGHT:
        new_pos[0][0] += grid_size
        if new_pos[0][0] >= SCREEN_WIDTH:
            new_pos[0][0] = 0

    current_pos.insert(0, [new_pos[0][0], new_pos[0][1]])
    current_pos.pop()

def handle_food_collision():
    global grape_x, grape_y, food_score, weight , end



    if current_pos[0] == [grape_x, grape_y]:
        end = time.time() + 5

        food_score += weight
        weight = random.randint(1, 3)
        play_music("food.mp3")
        
        wall_x, wall_y = generate_random_position()
        while [wall_x, wall_y] in current_pos:
            wall_x, wall_y = generate_random_position()
        walls.append([wall_x, wall_y])

        current_pos.append([grape_x, grape_y])
        
        while [grape_x, grape_y] in current_pos or [grape_x, grape_y] in walls:
            grape_x, grape_y = generate_random_position()

def game_over():
    if current_pos[0] in walls:
        theme_music.stop()
        play_music("gameover.mp3")
        screen.fill((10, 95, 56))
        draw_text("GAME OVER", 100, BLACK, (50, 150))
        draw_text(f"TOTAL SCORE: {food_score}", 30, GOLD, (200, 300))
        pygame.display.update()
        time.sleep(2)
        sys.exit()

def draw_elements():

    global end , grape_x , grape_y , weight

    

    screen.blit(background, (0, 0))
    
    if end - time.time() < 0 :
        end = time.time() + 5 

        grape_x , grape_y = generate_random_position()
        while [grape_x, grape_y] in current_pos or [grape_x, grape_y] in walls:
            grape_x, grape_y = generate_random_position()
        

        
        weight = random.randint( 1, 3 )
    
        
    
    pygame.draw.rect(screen, (134, 115, 161), (grape_x, grape_y, 50, 50))
    pygame.draw.rect(screen, (115, 81, 132), (grape_x, grape_y, 50, 50), 5)

    draw_text(str(weight), 50, BLACK, (grape_x+15 , grape_y-10))
    draw_text(f"Score: {food_score}", 20, GOLD, (3, 3))
    draw_text( str( int( end - time.time() )) , 20 , GOLD , ( 680  , 3 ) )
    
    for pos in current_pos:
        pygame.draw.rect(screen, GREEN, (*pos, grid_size, grid_size))
        pygame.draw.rect(screen, DARK_GREEN, (*pos, grid_size, grid_size), 5)
    
    for wall in walls:
        pygame.draw.rect(screen, RED, (*wall, grid_size, grid_size))
        pygame.draw.rect(screen, DARK_RED, (*wall, grid_size, grid_size), 5)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            play_music("move.mp3")
            if event.key == pygame.K_DOWN and direction != pygame.K_UP:
                direction = pygame.K_DOWN
            elif event.key == pygame.K_UP and direction != pygame.K_DOWN:
                direction = pygame.K_UP
            elif event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                direction = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                direction = pygame.K_RIGHT

    update_snake_position()
    handle_food_collision()
    game_over()
    draw_elements()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
