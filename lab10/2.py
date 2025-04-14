import pygame
import sys
import random
import time
import psycopg2

# ----------------------------
# 1. DATABASE CONNECTION SETUP
# ----------------------------

def create_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="MyDatabase",
            user="postgres",
            password="kbtu2025"
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            current_score INT DEFAULT 1
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL REFERENCES users(id),
            score INT NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()


def get_or_create_user(conn, username):
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    row = cur.fetchone()

    if row:
        user_id = row[0]
    else:
        cur.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING id",
            (username,)
        )
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    return user_id, 0  # Return the user_id and set the initial score to 0

def update_user_score(conn, user_id, score):
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET current_score = %s WHERE id = %s", (score, user_id))
        conn.commit()
        print(f"Score updated: User {user_id} score is now {score}")
    except Exception as e:
        print(f"Error updating score: {e}")
    finally:
        cur.close()

def save_score(conn, user_id, score):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_score (user_id, score) VALUES (%s, %s)",
        (user_id, score)
    )
    conn.commit()
    cur.close()

# ----------------------------
# 2. GAME CONSTANTS & VARIABLES
# ----------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 153, 0)
DARK_GREEN = (40, 114, 51)
RED = (205, 92, 92)
DARK_RED = (162, 35, 29)
GOLD = (255, 215, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600
GRID_SIZE = 50
FPS = 4

# ----------------------------
# 3. MAIN GAME FUNCTION
# ----------------------------

def solve():
    conn = create_connection()
    create_tables(conn)

    username = input("Enter your username: ")
    user_id, score = get_or_create_user(conn, username)
    print(f"Welcome, {username}! Your current score is {score}.")

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Load resources
    background = pygame.image.load("bg.jpg")
    theme_music = pygame.mixer.Sound("music.mp3")
    move_sound = "move.mp3"
    food_sound = "food.mp3"
    gameover_sound = "gameover.mp3"

    # Game state
    end_time = time.time() + 5
    theme_music.play(-1)

    snake = [[350, 300]]
    direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
    score = 0
    walls = []
    grape_x, grape_y = (random.randint(0, 13) * GRID_SIZE, random.randint(0, 11) * GRID_SIZE)
    weight = random.randint(1, 3)

    def draw_text(text, size, color, pos):
        font = pygame.font.SysFont("Comic Sans", size)
        surface = font.render(text, True, color)
        screen.blit(surface, pos)

    def play_music(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def generate_random_position():
        return random.randint(0, 13) * GRID_SIZE, random.randint(0, 11) * GRID_SIZE

    def update_snake_position():
        head_x, head_y = snake[0]
        if direction == pygame.K_DOWN:
            head_y += GRID_SIZE
        elif direction == pygame.K_UP:
            head_y -= GRID_SIZE
        elif direction == pygame.K_LEFT:
            head_x -= GRID_SIZE
        elif direction == pygame.K_RIGHT:
            head_x += GRID_SIZE

        head_x %= SCREEN_WIDTH
        head_y %= SCREEN_HEIGHT

        snake.insert(0, [head_x, head_y])
        snake.pop()

    def handle_food_collision():
        nonlocal grape_x, grape_y, score, weight, end_time

        if snake[0] == [grape_x, grape_y]:
            end_time = time.time() + 5
            score += weight
            weight = random.randint(1, 3)
            play_music(food_sound)

            wall_x, wall_y = generate_random_position()
            while [wall_x, wall_y] in snake:
                wall_x, wall_y = generate_random_position()
            walls.append([wall_x, wall_y])

            snake.append(snake[-1])

            while [grape_x, grape_y] in snake or [grape_x, grape_y] in walls:
                grape_x, grape_y = generate_random_position()

    def game_over():
        if snake[0] in walls:
            save_score(conn, user_id, score)
            theme_music.stop()
            play_music(gameover_sound)
            screen.fill((10, 95, 56))
            draw_text("GAME OVER", 100, BLACK, (50, 150))
            draw_text(f"TOTAL SCORE: {score}", 30, GOLD, (200, 300))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    def draw_elements():
        nonlocal end_time, grape_x, grape_y, weight

        screen.blit(background, (0, 0))

        if end_time - time.time() <= 0:
            end_time = time.time() + 5
            grape_x, grape_y = generate_random_position()
            while [grape_x, grape_y] in snake or [grape_x, grape_y] in walls:
                grape_x, grape_y = generate_random_position()
            weight = random.randint(1, 3)

        pygame.draw.rect(screen, (134, 115, 161), (grape_x, grape_y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, (115, 81, 132), (grape_x, grape_y, GRID_SIZE, GRID_SIZE), 5)
        draw_text(str(weight), 30, BLACK, (grape_x+15, grape_y+5))

        draw_text(f"Score: {score}", 20, GOLD, (5, 5))
        draw_text(str(int(end_time - time.time())), 20, GOLD, (SCREEN_WIDTH-40, 5))

        for pos in snake:
            pygame.draw.rect(screen, GREEN, (*pos, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, DARK_GREEN, (*pos, GRID_SIZE, GRID_SIZE), 5)

        for wall in walls:
            pygame.draw.rect(screen, RED, (*wall, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, DARK_RED, (*wall, GRID_SIZE, GRID_SIZE), 5)

    def pause_game():
        save_score(conn, user_id, score)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False

            screen.fill(BLACK)
            draw_text("Game Paused. Press 'P' to Resume.", 30, WHITE, (100, SCREEN_HEIGHT // 3))
            pygame.display.update()
            clock.tick(5)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(conn, user_id, score)
                running = False
            elif event.type == pygame.KEYDOWN:
                play_music(move_sound)
                if event.key == pygame.K_DOWN and direction != pygame.K_UP:
                    direction = pygame.K_DOWN
                elif event.key == pygame.K_UP and direction != pygame.K_DOWN:
                    direction = pygame.K_UP
                elif event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                    direction = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                    direction = pygame.K_RIGHT
                elif event.key == pygame.K_p:
                    pause_game()

        update_snake_position()
        handle_food_collision()
        game_over()
        draw_elements()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    solve()
