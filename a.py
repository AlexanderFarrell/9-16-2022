import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    pygame.display.flip()
    pygame.time.wait(17)


pygame.quit()