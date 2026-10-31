import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
SPRITE_SIZE = 30
RED = pygame.Color("red")
BLUE =    pygame.Color("blue")
X_CHANGE, Y_CHANGE = 0, 0
SCORE = 0
win = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("More Sprites")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, X, Y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(colour))
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y


player = Sprite(BLUE, SPRITE_SIZE, SPRITE_SIZE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

enemies_group = pygame.sprite.Group()
number_of_enemies = 7
for i in range(number_of_enemies):
    enemy = Sprite(RED, SPRITE_SIZE, SPRITE_SIZE, random.randint(0, SCREEN_WIDTH - SPRITE_SIZE), random.randint(0, SCREEN_HEIGHT - SPRITE_SIZE))
    enemies_group.add(enemy)

all_sprites = pygame.sprite.Group()
all_sprites.add(enemies_group)
all_sprites.add(player)

def win_screen():
    global win
    win = True
    font = pygame.font.Font("freesansbold.ttf", 64)
    win_text = font.render("YOU WIN", True, (255, 255, 255))
    win_rect = win_text.get_rect()
    win_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    return win_text, win_rect

def show_score(score):
    font = pygame.font.Font("freesansbold.ttf", 32)
    return font.render("Score: " + str(score), True, (255, 255, 255))

    

    

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and win == False:
            if event.key == pygame.K_LEFT:
                X_CHANGE -= 5
            elif event.key == pygame.K_RIGHT:
                X_CHANGE += 5
            elif event.key == pygame.K_UP:
                Y_CHANGE -= 5
            elif event.key == pygame.K_DOWN:
                Y_CHANGE += 5
        elif event.type == pygame.KEYUP and win == False:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                X_CHANGE = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                Y_CHANGE = 0

    player.rect.x += X_CHANGE
    player.rect.y += Y_CHANGE
    player.rect.x = max(0, min(player.rect.x, SCREEN_WIDTH - SPRITE_SIZE))
    player.rect.y = max(0, min(player.rect.y, SCREEN_HEIGHT - SPRITE_SIZE))

    for enemy in enemies_group:
        if enemy.rect.colliderect(player) and enemy in all_sprites:
            enemy.kill()
            SCORE += 1
    if not enemies_group:
        text, position = win_screen()
        screen.blit(text, position)

    screen.blit(show_score(SCORE), (10, 10))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()