from ursina import *
from random import uniform

app = Ursina()

# === Set up player ===
player = Entity(model='cube', color=color.azure, scale=(1, 2, 1), position=(0, 1, -5))
camera.parent = player
camera.position = (0, 1.5, 0)
camera.rotation = (0, 0, 0)
mouse.locked = True

# === Environment ===
ground = Entity(model='plane', scale=(50,1,50), texture='white_cube', texture_scale=(50,50), collider='box')
Sky()

# === Enemy Setup ===
enemies = []

def spawn_enemy():
    enemy = Entity(
        model='cube',
        color=color.red,
        scale=1,
        position=(uniform(-10, 10), 1, uniform(5, 20)),
        collider='box'
    )
    enemies.append(enemy)

for _ in range(10):
    spawn_enemy()

# === Bullets ===
bullets = []

def shoot():
    bullet = Entity(
        model='sphere',
        color=color.yellow,
        scale=0.2,
        position=player.position + Vec3(0, 1, 1),
        collider='sphere'
    )
    bullet.forward = camera.forward
    bullets.append(bullet)

# === Player Movement ===
speed = 5
mouse_sensitivity = Vec2(40, 40)

def update():
    # Movement
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    player.position += direction * time.dt * speed
    player.rotation_y += mouse.velocity[0] * mouse_sensitivity[0]

    # Shooting bullets
    for bullet in bullets:
        bullet.position += bullet.forward * time.dt * 20
        hit_info = bullet.intersects()
        if hit_info.hit:
            if hit_info.entity in enemies:
                enemies.remove(hit_info.entity)
                destroy(hit_info.entity)
            destroy(bullet)
            bullets.remove(bullet)
            break

def input(key):
    if key == 'left mouse down':
        shoot()
    elif key == 'escape':
        mouse.locked = False
    elif key == 'tab':
        mouse.locked = True

app.run()
