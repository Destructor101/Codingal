import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SPRITE_SIZE = 64
X_change, Y_change = 0, 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesssss")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, X, Y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y


sp1 = Sprite((0, 0, 0), SPRITE_SIZE, SPRITE_SIZE, random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT - 64))
sp2 = Sprite((255, 0, 0), SPRITE_SIZE, SPRITE_SIZE, random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT - 64))

all_sprites = pygame.sprite.Group()
for sprite in [sp1, sp2]:
    all_sprites.add(sprite)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_change = -5
            if event.key == pygame.K_RIGHT:
                X_change = +5
            if event.key == pygame.K_UP:
                Y_change = -5
            if event.key == pygame.K_DOWN:
                Y_change = +5
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                X_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                Y_change = 0

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    sp1.rect.x += X_change
    sp1.rect.y += Y_change

    pygame.display.flip()
    clock.tick(90)

pygame.quit()

