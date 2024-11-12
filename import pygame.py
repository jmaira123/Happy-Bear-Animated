import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Happy Bear Animation')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (210, 180, 140)
DARK_BROWN = (101, 67, 33)
SKY_BLUE = (135, 206, 250)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)

# Function to draw a happy bear character
def draw_happy_bear(surface, x, y):
    # Draw head
    pygame.draw.circle(surface, BROWN, (x + 50, y + 50), 40)  # Bear head
    pygame.draw.circle(surface, DARK_BROWN, (x + 50, y + 50), 40, 2)  # Head outline

    # Draw ears
    pygame.draw.circle(surface, BROWN, (x + 20, y + 30), 15)  # Left ear
    pygame.draw.circle(surface, BROWN, (x + 80, y + 30), 15)  # Right ear
    pygame.draw.circle(surface, DARK_BROWN, (x + 20, y + 30), 15, 2)  # Left ear outline
    pygame.draw.circle(surface, DARK_BROWN, (x + 80, y + 30), 15, 2)  # Right ear outline

    # Draw face details
    pygame.draw.circle(surface, LIGHT_BROWN, (x + 50, y + 60), 15)  # Nose
    pygame.draw.circle(surface, BLACK, (x + 50, y + 60), 8)  # Nose outline

    # Draw eyes
    pygame.draw.circle(surface, WHITE, (x + 35, y + 45), 8)   # Left eye
    pygame.draw.circle(surface, WHITE, (x + 65, y + 45), 8)   # Right eye
    pygame.draw.circle(surface, BLACK, (x + 35, y + 45), 4)   # Left pupil
    pygame.draw.circle(surface, BLACK, (x + 65, y + 45), 4)   # Right pupil

    # Draw happy mouth
    pygame.draw.arc(surface, BLACK, (x + 35, y + 70, 30, 15), 0, 3.14, 2)  # Smile
    pygame.draw.line(surface, BLACK, (x + 35, y + 78), (x + 65, y + 78), 2)  # Smile extension

    # Draw body (rounded rectangle)
    pygame.draw.rect(surface, BROWN, (x + 30, y + 90, 40, 70), border_radius=20)  # Body

    # Draw arms
    pygame.draw.circle(surface, BROWN, (x + 15, y + 90), 15)  # Left arm
    pygame.draw.circle(surface, BROWN, (x + 85, y + 90), 15)  # Right arm

    # Draw legs
    pygame.draw.circle(surface, BROWN, (x + 35, y + 160), 15)  # Left leg
    pygame.draw.circle(surface, BROWN, (x + 65, y + 160), 15)  # Right leg

# Function to draw a colorful background
def draw_background(surface):
    # Draw sky
    surface.fill(SKY_BLUE)

    # Draw ground
    pygame.draw.rect(surface, GREEN, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Draw sun
    pygame.draw.circle(surface, YELLOW, (700, 100), 50)  # Sun

    # Draw clouds
    pygame.draw.ellipse(surface, WHITE, (100, 50, 100, 50))  # Cloud 1
    pygame.draw.ellipse(surface, WHITE, (150, 70, 100, 50))  # Cloud 1
    pygame.draw.ellipse(surface, WHITE, (500, 30, 100, 50))  # Cloud 2
    pygame.draw.ellipse(surface, WHITE, (550, 50, 100, 50))  # Cloud 2

def main():
    clock = pygame.time.Clock()
    running = True
    x, y = WIDTH // 2 - 50, HEIGHT // 2 - 100  # Start position of the bear
    direction = 1  # Movement direction

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update position
        y += direction
        if y > HEIGHT - 200 or y < 0:
            direction *= -1

        # Clear the screen
        draw_background(window)

        # Draw the happy bear character
        draw_happy_bear(window, x, y)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
