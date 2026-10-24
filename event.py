import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SPRITE_SIZE = 64
colours = [pygame.Color("red"), pygame.Color("blue"), pygame.Color("white"), pygame.Color("yellow"), pygame.Color("pink")]
CHANGE_COLOUR_EVENT = pygame.USEREVENT + 1
MAX_SPEED = 7

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, X, Y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        pygame.draw.rect(self.image, colour, pygame.Rect(X, Y, width, height))
        self.rect = self.image.get_rect()
        self.x_velocity = random.randint(-MAX_SPEED, MAX_SPEED)
        if self.x_velocity == 0:
            self.x_velocity = 1
        self.y_velocity = random.randint(-MAX_SPEED, MAX_SPEED)
        if self.y_velocity == 0:
            self.y_velocity = 1

sp1 = Sprite(random.choice(colours), SPRITE_SIZE, SPRITE_SIZE, random.randint(0, SCREEN_WIDTH - SPRITE_SIZE), random.randint(0, SCREEN_HEIGHT - SPRITE_SIZE))
sp2 = Sprite(random.choice(colours), SPRITE_SIZE, SPRITE_SIZE, random.randint(0, SCREEN_WIDTH - SPRITE_SIZE), random.randint(0, SCREEN_HEIGHT - SPRITE_SIZE))

all_sprites = pygame.sprite.Group()
for sprite in [sp1, sp2]:
    all_sprites.add(sprite)

in_collision = False
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOUR_EVENT:
            sp1.image.fill(random.choice(colours))
            sp2.image.fill(random.choice(colours))

    if sp1.rect.colliderect(sp2.rect) and in_collision == False:
        pygame.event.post(pygame.event.Event(CHANGE_COLOUR_EVENT))
        in_collision = True
    elif not sp1.rect.colliderect(sp2.rect) and in_collision == True:
        in_collision = False

    for sprite in [sp1, sp2]:
        sprite.rect.x += sprite.x_velocity 
        sprite.rect.y += sprite.y_velocity

        if sprite.rect.x <= 0:
            sprite.x_velocity *= -1
            sprite.rect.x = 1
        elif sprite.rect.x >= SCREEN_WIDTH - SPRITE_SIZE:
            sprite.rect.x = SCREEN_WIDTH - SPRITE_SIZE - 1
            sprite.x_velocity *= -1
     
        if sprite.rect.y <= 0:
            sprite.y_velocity *= -1
            sprite.rect.y = 1
        elif sprite.rect.y >= SCREEN_HEIGHT - SPRITE_SIZE:
            sprite.y_velocity *= -1
            sprite.rect.y = SCREEN_HEIGHT - SPRITE_SIZE - 1
        


    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)