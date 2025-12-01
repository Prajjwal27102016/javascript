import pygame
import sys  # Added for proper exit handling


# Initialize Pygame
pygame.init()


# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500


# Create display surface
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')


# Load and scale images
try:
   background_image = pygame.transform.scale(
       pygame.image.load('background.png').convert(),
       (SCREEN_WIDTH, SCREEN_HEIGHT))
  
   penguin_image = pygame.transform.scale(
       pygame.image.load('penguin.png').convert_alpha(),
       (200, 200))
except FileNotFoundError as e:
   print(f"Error loading image: {e}")
   pygame.quit()
   sys.exit()


# Position images
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                           SCREEN_HEIGHT // 2 - 30))


# Create text
font = pygame.font.Font(None, 36)  # Store font for reuse
text = font.render('Hello Prajjwal Singh Mandloi !', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


def game_loop():
   clock = pygame.time.Clock()
   running = True
  
   while running:
       # Event handling
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
      
       # Rendering
       display_surface.blit(background_image, (0, 0))  # Draw background first
       display_surface.blit(penguin_image, penguin_rect)  # Then penguin
       display_surface.blit(text, text_rect)  # Finally text
      
       pygame.display.flip()  # Update display
       clock.tick(30)  # 30 FPS
  
   pygame.quit()
   sys.exit()  # Clean exit


if __name__ == '__main__':
   game_loop()
