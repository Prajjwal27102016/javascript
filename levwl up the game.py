import pygame
import random
import os # Import os module to handle file paths
import sys
# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 1 // 90 # Adjusted for frame rate
FONT_SIZE = 72


# Initialize Pygame
pygame.init()


# --- Correction/Improvement 1: Handle background image loading ---
# Check if bg.jpg exists. If not, create a solid color background.
BACKGROUND_IMAGE_PATH = "world-map.png"
if os.path.exists(BACKGROUND_IMAGE_PATH):
   background_image = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE_PATH),
                                             (SCREEN_WIDTH, SCREEN_HEIGHT))
else:
   print(f"Warning: '{BACKGROUND_IMAGE_PATH}' not found. Using a solid blue background.")
   background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
   background_image.fill(pygame.Color('skyblue')) # Default solid background color


# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):


 def __init__(self, color, height, width):
   super().__init__()
   self.image = pygame.Surface([width, height])
   # --- Correction/Improvement 2: Remove redundant fill ---
   # The self.image.fill() line below was redundant because pygame.draw.rect()
   # would immediately cover the entire surface with the 'color' anyway.
   # We directly fill the surface with the desired 'color'.
   self.image.fill(color)
   # If you intended a border, you would draw a smaller rect inside,
   # or use a different shape. For a solid color sprite, just fill.


   self.rect = self.image.get_rect()


 def move(self, x_change, y_change):
   # Ensure sprite stays within screen bounds
   self.rect.x = max(
       min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
   self.rect.y = max(
       min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)




# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group() # Group to hold all sprites for drawing and updates


# Create sprites
# sprite1 is the player-controlled sprite
sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1) # Add sprite1 to the group


# sprite2 is the target sprite
sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2) # Add sprite2 to the group


# Game loop control variables
running = True # Controls if the main game loop is active
won = False    # Flag to indicate if the player has won
clock = pygame.time.Clock() # Used to control the game's frame rate


# Main game loop
while running:
 # Event handling loop
 for event in pygame.event.get():
   # Check for quit event (closing the window)
   if event.type == pygame.QUIT:
     running = False
   # Check for 'x' key press to quit
   elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
     running = False


 # Game logic (only run if the game hasn't been won yet)
 if not won:
   # Get all currently pressed keys
   keys = pygame.key.get_pressed()
   # Calculate movement based on arrow keys
   x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
   y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
   # Move sprite1 based on calculated changes
   sprite1.move(x_change, y_change)


   # Check for collision between sprite1 and sprite2
   if sprite1.rect.colliderect(sprite2.rect):
     all_sprites.remove(sprite2) # Remove sprite2 from the drawing group
     won = True # Set win flag to True


 # Drawing section
 screen.blit(background_image, (0, 0)) # Draw the background image


 # Draw all sprites currently in the all_sprites group
 all_sprites.draw(screen)


 # Display win message if the game is won
 if won:
   # Render the "You win!" text
   win_text = font.render("You win!", True, pygame.Color('black'))
   # Calculate position to center the text
   text_x = (SCREEN_WIDTH - win_text.get_width()) // 2
   text_y = (SCREEN_HEIGHT - win_text.get_height()) // 2
   screen.blit(win_text, (text_x, text_y)) # Draw the win message


 pygame.display.flip() # Update the entire screen to show what has been drawn
 clock.tick(90) # Limit the frame rate to 90 frames per second


pygame.quit() # Uninitialize Pygame modules
