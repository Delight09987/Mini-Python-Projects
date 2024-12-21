import pygame as pg
import sys

# Initialize pygame
pg.init()

# Set up display
flag = pg.NOFRAME  # Use NOFRAME for window without borders (optional)
screen = pg.display.set_mode((700, 800), flag)
pg.display.set_caption("Basketball Backboard")

# Define background color (black)
background_color = pg.Color(0, 0, 0)

# Clock for controlling the frame rate
clock = pg.time.Clock()

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Draw the backboard
    backboard_color = (255, 255, 255)  # White
    pg.draw.rect(screen, backboard_color, [200, 150, 300, 150], 0)  # Main backboard
    
    # Draw the shooter's square on the backboard
    square_color = (200, 0, 0)  # Red
    pg.draw.rect(screen, square_color, [280, 200, 140, 50], 5)  # Inner rectangle
    
    # Draw the rim
    rim_color = (255, 140, 0)  # Orange
    pg.draw.circle(screen, rim_color, (350, 280), 45, 5)  # Circle for rim
    
    # Update the display
    pg.display.update()
    
    # Limit frame rate to 60 FPS
    clock.tick(60)

# Quit the game and close the window
pg.quit()
sys.exit()