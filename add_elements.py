import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
rectangle = pygame.rect.Rect(62, 172, 517, 137)

font = pygame.font.SysFont(None, 20)
text_surface = font.render("This be some rectangle idk", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), rectangle)
    screen.blit(text_surface, (240, 240))

    pygame.display.flip()

pygame.quit()