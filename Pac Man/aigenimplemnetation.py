import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((640, 480))

# Load the images
pacman_image = pygame.image.load("pacman.png")
ghost_image = pygame.image.load("ghost.png")

# Create the pacman and ghost objects
pacman = pygame.sprite.Sprite()
pacman.image = pacman_image
pacman.rect = pacman_image.get_rect()

ghost = pygame.sprite.Sprite()
ghost.image = ghost_image
ghost.rect = ghost_image.get_rect()

# Create the maze
maze = pygame.sprite.Group()
for i in range(0, 20):
    for j in range(0, 15):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            wall = pygame.sprite.Sprite()
            wall.image = pygame.Surface((10, 10))
            wall.rect = wall.image.get_rect()
            wall.rect.x = i * 10
            wall.rect.y = j * 10
            maze.add(wall)

# Create the event loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the pacman
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                pacman.rect.x += 10
            elif event.key == pygame.K_UP:
                pacman.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                pacman.rect.y += 10

    # Check for collisions
    collisions = pygame.sprite.spritecollide(pacman, maze, False)
    if collisions:
        # If pacman collides with a wall, stop him
        for wall in collisions:
            pacman.rect.x = wall.rect.x - pacman.rect.width
            pacman.rect.y = wall.rect.y - pacman.rect.height

    collisions = pygame.sprite.spritecollide(pacman, ghost, False)
    if collisions:
        # If pacman collides with a ghost, game over
        running = False

    # Draw the screen
    screen.fill((0, 0, 0))
    maze.draw(screen)
    pacman.draw(screen)
    ghost.draw(screen)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
