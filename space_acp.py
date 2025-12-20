import math
import random
import pygame
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 4
BULLET_SPEED_Y =20
COLLISION_DISTANCE = 27
ENEMY_SIZE = 50
BULLET_SIZE = 20

# Runtime-adjustable settings (can be changed while the game runs)
PLAYER_SPEED = 5          # used for left/right movement
enemy_speed = 4  # initial enemy horizontal speed
enemy_size = ENEMY_SIZE
bullet_size = BULLET_SIZE
bullet_speed = BULLET_SPEED_Y
collision_distance = int(enemy_size * 0.42)


# Initialize Pygame
pygame.init()

# 🎶 Initialize the mixer for sound
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Helper to load images safely and provide a placeholder if missing
def load_image(path, size=None):
    if os.path.isfile(path):
        try:
            img = pygame.image.load(path)
            if size:
                img = pygame.transform.scale(img, size)
            return img
        except Exception as e:
            print(f"Could not load image '{path}': {e}")
    else:
        print(f"Image file not found: {path}")
    # Create a visible placeholder surface for missing images
    w, h = size if size else (64, 64)
    placeholder = pygame.Surface((w, h))
    placeholder.fill((255, 0, 255))  # magenta indicates missing asset
    return placeholder

# Background
background = load_image('i2.jpg', (SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = load_image('choclateremovebgpreview.png')
pygame.display.set_icon(icon)

# --- Sound Setup ---

# Background Music
bg_music = 'backgroundmusic.wav'
if os.path.isfile(bg_music):
    try:
        pygame.mixer.music.load(bg_music)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Could not load background music: {e}")
else:
    print(f"Background music file not found: {bg_music}")

# Sound Effects - safe loading with fallback
class _DummySound:
    def play(self):
        pass

def load_sound(filename):
    if os.path.isfile(filename):
        try:
            return pygame.mixer.Sound(filename)
        except Exception as e:
            print(f"Could not load sound '{filename}': {e}")
            return _DummySound()
    else:
        print(f"Sound file not found: {filename}")
        return _DummySound()

# Update these filenames to match your files in the project directory
bullet_sound = load_sound('bullet.wav')
explosion_sound = load_sound('explosionsound.wav')


# Player
playerImg = load_image('astropro.jpeg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Load base enemy image and create scaled copies so we can resize at runtime
enemy_base_img = load_image('enemy.png')
for _i in range(num_of_enemies):
    img = pygame.transform.scale(enemy_base_img, (enemy_size, enemy_size))
    enemyImg.append(img)
    enemyX.append(random.randint(0, SCREEN_WIDTH - enemy_size))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    # Give some enemies negative direction to spread them out
    enemyX_change.append(enemy_speed if random.choice([True, False]) else -enemy_speed)
    enemyY_change.append(ENEMY_SPEED_Y)

# Helper to apply current enemy_speed to all enemies (preserves direction)
def apply_enemy_speed():
    for k in range(len(enemyX_change)):
        sign = 1 if enemyX_change[k] >= 0 else -1
        enemyX_change[k] = sign * enemy_speed

# Bullet
bulletImg = load_image('gun.bullet2.png', (bullet_size, bullet_size))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_debug():
    # Show current adjustable settings and key help
    lines = [
        f"Player speed (q/a): {PLAYER_SPEED}",
        f"Enemy speed (w/s): {enemy_speed}",
        f"Enemy size (e/d): {enemy_size}",
        f"Bullet speed (r/f): {bullet_speed}",
        f"Bullet size: {bullet_size}",
        "Keys: q/a player, w/s enemy, e/d size, r/f bullet"
    ]
    for i, line in enumerate(lines):
        txt = font.render(line, True, (255, 255, 0))
        screen.blit(txt, (10, SCREEN_HEIGHT - (len(lines) - i) * 20 - 10))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < collision_distance

# Game loop
running = True
while running:
    # Set the background image (this was already present, but is crucial)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED
            # 🔊 Play bullet sound when space is pressed and bullet is ready
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound.play() # Play the sound effect
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

            # Runtime controls (press keys during the game):
            if event.key == pygame.K_q:  # Increase player speed
                PLAYER_SPEED += 1
            if event.key == pygame.K_a:  # Decrease player speed
                PLAYER_SPEED = max(1, PLAYER_SPEED - 1)

            if event.key == pygame.K_w:  # Increase enemy speed
                enemy_speed += 1
                apply_enemy_speed()
            if event.key == pygame.K_s:  # Decrease enemy speed
                enemy_speed = max(1, enemy_speed - 1)
                apply_enemy_speed()
            if event.key == pygame.K_z:  # Re-apply current enemy speed to all enemies
                apply_enemy_speed()

            if event.key == pygame.K_e:  # Increase enemy size
                enemy_size += 8
                collision_distance = int(enemy_size * 0.42)
                for k in range(len(enemyImg)):
                    enemyImg[k] = pygame.transform.scale(enemy_base_img, (enemy_size, enemy_size))
            if event.key == pygame.K_d:  # Decrease enemy size
                enemy_size = max(16, enemy_size - 8)
                collision_distance = int(enemy_size * 0.42)
                for k in range(len(enemyImg)):
                    enemyImg[k] = pygame.transform.scale(enemy_base_img, (enemy_size, enemy_size))

            if event.key == pygame.K_r:  # Increase bullet speed
                bullet_speed += 1
            if event.key == pygame.K_f:  # Decrease bullet speed
                bullet_speed = max(1, bullet_speed - 1)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - enemy_size:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            # 💥 Play explosion sound upon collision
            explosion_sound.play()
            
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            # Reset enemy position
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_speed

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()