from ursina import *
from random import randint, uniform

app = Ursina()
window.color = color.black

# Player (the cube)
player = Entity(model='cube', color=color.cyan, scale=(1,1,1), position=(-5, 0, 0), collider='box')
gravity = -0.04
velocity_y = 0
on_ground = True

# Floor
ground = Entity(model='cube', color=color.gray, scale=(100,1,1), position=(0, -1, 0), collider='box')

# Obstacles
obstacles = []

def spawn_obstacle():
    x = 20 + uniform(2, 5)
    obstacle = Entity(model='cube', color=color.red, scale=(1,2,1), position=(x, 0, 0), collider='box')
    obstacles.append(obstacle)

for _ in range(5):
    spawn_obstacle()

# Score
score = 0
score_text = Text(text=f"Score: {score}", position=window.top_left, origin=(-0.5, 0.5), scale=1.5)

# Game Over Text
game_over_text = Text('', origin=(0,0), scale=2, enabled=False)

# Update Loop
def update():
    global velocity_y, on_ground, score

    # Apply gravity
    player.y += velocity_y
    velocity_y += gravity

    # Floor collision
    if player.y <= 0:
        player.y = 0
        velocity_y = 0
        on_ground = True

    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= 0.1
        if obstacle.x < -20:
            obstacle.x = 20 + uniform(2, 5)
            score += 1
            score_text.text = f"Score: {score}"

        # Collision detection
        if player.intersects(obstacle).hit:
            game_over()

def input(key):
    global velocity_y, on_ground
    if key == 'space' and on_ground:
        velocity_y = 0.9
        on_ground = False
    if key == 'r':
        restart_game()

def game_over():
    application.pause()
    game_over_text.text = 'Game Over! Press R to restart.'
    game_over_text.enabled = True

def restart_game():
    global score
    application.resume()
    player.y = 0
    velocity_y = 0
    score = 0
    score_text.text = f"Score: {score}"
    game_over_text.enabled = False
    for obstacle in obstacles:
        obstacle.x = 20 + uniform(2, 5)

app.run()
