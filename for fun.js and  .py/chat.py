from ursina import *

app = Ursina()

# Define player
player = Entity(model='cube', color=color.orange, scale_y=2, position=(0, 1, 0), collider='box')

# Define the ground
ground = Entity(model='plane', scale=(100,1,100), color=color.green, collider='box')

# Add a sky
Sky()

# Add some lighting
DirectionalLight(y=2, z=3, shadows=True)

# Gravity and movement
player_speed = 5
jump_height = 0.2
is_jumping = False
velocity_y = 0

def update():
    global is_jumping, velocity_y

    # Move player
    move = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized() * time.dt * player_speed
    player.position += move

    # Simple gravity
    velocity_y -= 0.01
    player.y += velocity_y

    # Ground collision
    if player.y < 1:
        player.y = 1
        velocity_y = 0
        is_jumping = False

    # Jumping
    if not is_jumping and held_keys['space']:
        is_jumping = True
        velocity_y = jump_height

app.run()
