from ursina import *
from random import uniform

app = Ursina()

# === Player and Camera ===
player = Entity(model='cube', color=color.azure, scale_y=2, position=(0, 1, 0), collider='box')
camera.parent = player
camera.position = (0, 1.5, 0)
camera.rotation = (0, 0, 0)
mouse.locked = True

# === Ground and Environment ===
ground = Entity(model='plane', scale=(50,1,50), texture='white_cube', texture_scale=(50,50), collider='box')
Sky()

# === Bullet System ===
bullets = []

def shoot():
    bullet = Entity(model='sphere', color=color.yellow, scale=0.2, position=player.position + Vec3(0, 1.5, 0), collider='sphere')
    bullet.forward = camera.forward
    bullets.append(bullet)

# === Zombie Enemy System ===
class Zombie(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            color=color.green,
            position=position,
            scale_y=2,
            collider='box',
            health=3
        )

    def update(self):
        self.look_at(player, 'forward')
        self.position += self.forward * time.dt * 1.2

zombies = [Zombie(position=(uniform(-10,10),1,uniform(5,25))) for _ in range(5)]

# === Player Health ===
player_health = 5
health_text = Text(text=f"Health: {player_health}", position=window.top_left, origin=(-0.5,0.5), scale=1.5)

# === Update Loop ===
def update():
    global player_health

    # Player movement
    direction = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s']).normalized()
    player.position += direction * time.dt * 5
    player.rotation_y += mouse.velocity[0] * 40

    # Move bullets and check for hits
    for bullet in bullets[:]:
        bullet.position += bullet.forward * time.dt * 20
        for zombie in zombies:
            if bullet.intersects(zombie).hit:
                zombie.health -= 1
                destroy(bullet)
                bullets.remove(bullet)
                if zombie.health <= 0:
                    zombies.remove(zombie)
                    destroy(zombie)
                break

    # Zombies attack
    for zombie in zombies:
        if distance(zombie.position, player.position) < 1.5:
            player_health -= 1
            health_text.text = f"Health: {player_health}"
            player.color = color.red
            invoke(setattr, player, 'color', color.azure, delay=0.3)
            zombies.remove(zombie)
            destroy(zombie)
            if player_health <= 0:
                application.quit()

def input(key):
    if key == 'left mouse down':
        shoot()
    if key == 'escape':
        mouse.locked = False
    if key == 'tab':
        mouse.locked = True

app.run()
w