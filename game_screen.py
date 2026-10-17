import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")
image = pygame.rect.Rect(100, 100, 300, 300)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (58, 58, 58), image)
    pygame.display.flip()

pygame.quit()