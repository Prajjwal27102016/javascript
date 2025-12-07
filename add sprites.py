import pygame
import random
import sys # Recommended for sys.exit()


# Initialize Pygame
pygame.init()


# --- Constants ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 20
FPS = 60 # Frames per second


# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2


# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')


# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')




# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
   # Constructor method
   def __init__(self, color, height, width, screen_w, screen_h, speed=50):
       # Call to the parent class (Sprite) constructor
       super().__init__()
       # Store screen dimensions for boundary checks
       self.screen_width = screen_w
       self.screen_height = screen_h
      
       # Create the sprite's surface with dimensions and color
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       # Get the sprite's rect defining its position and size
       self.rect = self.image.get_rect()
      
       # Set initial velocity with random direction and configurable speed
       self.speed = speed
       self.velocity = [random.choice([-1, 1]) * self.speed,
                        random.choice([-1, 1]) * self.speed]
       # Ensure it's not starting with zero velocity if speed could be zero,
       # but here speed is positive. If both components were 0, it wouldn't move.
       if self.velocity == [0,0]: # Highly unlikely with current setup but good for robustness
           self.velocity = [self.speed, self.speed]




   # Method to update the sprite's position
   def update(self):
       # Move the sprite by its velocity
       self.rect.move_ip(self.velocity)
      
       boundary_hit = False
      
       # Check for collision with left or right boundaries and reverse direction
       if self.rect.left <= 0:
           self.rect.left = 0 # Clamp to boundary
           self.velocity[0] = -self.velocity[0]
           boundary_hit = True
       elif self.rect.right >= self.screen_width:
           self.rect.right = self.screen_width # Clamp to boundary
           self.velocity[0] = -self.velocity[0]
           boundary_hit = True
          
       # Check for collision with top or bottom boundaries and reverse direction
       if self.rect.top <= 0:
           self.rect.top = 0 # Clamp to boundary
           self.velocity[1] = -self.velocity[1]
           boundary_hit = True
       elif self.rect.bottom >= self.screen_height:
           self.rect.bottom = self.screen_height # Clamp to boundary
           self.velocity[1] = -self.velocity[1]
           boundary_hit = True


       # If a boundary was hit, post events to change colors
       if boundary_hit:
           pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
           pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))


   # Method to change the sprite's color
   def change_color(self):
       new_color = random.choice([YELLOW, MAGENTA, ORANGE, WHITE])
       # Ensure the new color is different from the current one, if possible
       # This is a minor addition, can be removed if not desired
       current_color = self.image.get_at((0,0))
       available_colors = [c for c in [YELLOW, MAGENTA, ORANGE, WHITE] if c != current_color]
       if available_colors:
           new_color = random.choice(available_colors)
       self.image.fill(new_color)




# Function to change the background color
def change_background_color():
   global bg_color # Using global here is acceptable for this script's size
  
   new_bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
   # Ensure the new background color is different from the current one, if possible
   available_bg_colors = [c for c in [BLUE, LIGHTBLUE, DARKBLUE] if c != bg_color]
   if available_bg_colors:
       new_bg_color = random.choice(available_bg_colors)
   bg_color = new_bg_color




# --- Game Setup ---
# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()


# Instantiate the sprite, passing screen dimensions and desired speed
sp1 = Sprite(WHITE, SPRITE_HEIGHT, SPRITE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, speed=100000000000000)


# Randomly position the sprite ensuring it's fully on screen
sp1.rect.x = random.randint(0, SCREEN_WIDTH - sp1.rect.width)
sp1.rect.y = random.randint(0, SCREEN_HEIGHT - sp1.rect.height)


# Add the sprite to the group
all_sprites_list.add(sp1)


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the window title
pygame.display.set_caption("Colorful Bounce")
# Set the initial background color
bg_color = BLUE


# Game loop control flag
running = True
# Create a clock object to control frame rate
clock = pygame.time.Clock()


# --- Main Game Loop ---
while running:
   # Event handling loop
   for event in pygame.event.get():
       # If the window's close button is clicked, exit the game
       if event.type == pygame.QUIT:
           running = False
       # If the sprite color change event is triggered, change the sprite's color
       elif event.type == SPRITE_COLOR_CHANGE_EVENT:
           sp1.change_color() # sp1 is the specific instance
       # If the background color change event is triggered, change the background color
       elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
           change_background_color()


   # Update all sprites
   all_sprites_list.update()
  
   # Drawing code
   screen.fill(bg_color) # Fill the screen with the current background color
   all_sprites_list.draw(screen) # Draw all sprites to the screen


   # Refresh the display
   pygame.display.flip()
   # Limit the frame rate
   clock.tick(FPS)


# Uninitialize all pygame modules and close the window
pygame.quit()
sys.exit() # Ensures the program closes properly