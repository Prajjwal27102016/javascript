import pygame
import random

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(random_color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    sprite1 = ColorSprite(200, 200, (255, 0, 0))
    sprite2 = ColorSprite(400, 200, (0, 0, 255))
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite1)
    all_sprites.add(sprite2)

    pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CHANGE_COLOR_EVENT:
                for sprite in all_sprites:
                    sprite.change_color()

        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()