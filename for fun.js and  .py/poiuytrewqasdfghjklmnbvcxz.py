import pygame
import sys

pygame.init()

window_width = 500
window_height = 500
screen_size = (window_width, window_height)

grey = (58, 58, 58)

image_width = 300
image_height = 300
image_file = 'my_image.png'

caption = "My first game screen"

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(caption)

try:
    original_image = pygame.image.load(image_file)
    image = pygame.transform.scale(original_image, (image_width, image_height))
    image_rect = image.get_rect()
    image_rect.center = screen.get_rect().center
    
except pygame.error as e:
    print(f"Error loading or transforming image: {e}")
    print(f"Make sure '{image_file}' is in the same directory as the script.")
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(grey)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()