import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
birdL_image = pygame.image.load("birdL.jpg")
birdR_image = pygame.image.load("birdR.jpg")
background_image = pygame.image.load("background.png")
pipe_image = pygame.image.load("pipe.png")


# Bird class
class Bird:
    def __init__(self):
        self.image = birdL_image
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0
        self.gravity = 0.5
        self.flap_power = -10
        self.bird_direction = 1

    def update(self):
        self.velocity += self.gravity
        self.rect.centery += self.velocity

    def flap(self):
        self.velocity = self.flap_power
        self.bird_direction = self.bird_direction * -1
        if self.bird_direction == -1:
            self.image = birdL_image
        else:
            self.image = birdR_image

    def draw(self):
        screen.blit(self.image, self.rect)


# Pipe class
class Pipe:
    def __init__(self, x, y):
        self.image = pipe_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.passed = False

    def update(self):
        self.rect.x -= 5

    def draw(self):
        screen.blit(self.image, self.rect)


def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Update game objects
        bird.update()

        # Add pipes
        if random.randint(1, 100) == 1:
            pipe_y = random.randint(100, 400)
            pipes.append(Pipe(SCREEN_WIDTH, pipe_y))

        # Update pipes
        for pipe in pipes:
            pipe.update()
            if pipe.rect.right < 0:
                pipes.remove(pipe)
                score += 1

        # Draw everything
        screen.blit(background_image, (0, 0))
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
