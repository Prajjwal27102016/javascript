import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("My Game Screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 50)
text_surface = font.render("Hello Pygame!", True, BLACK)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (100, 150, 200, 100))

    screen.blit(text_surface, (100, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()