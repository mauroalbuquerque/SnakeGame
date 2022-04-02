import sys, pygame

pygame.init()

size = width, height = 1000, 500

color_bg = 0, 0, 0

screen = pygame.display.set_mode(size)

block = pygame.image.load("resources/body.jpg")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #screen.fill(color_bg)
    screen.blit(block, [100, 100])
    pygame.display.flip()