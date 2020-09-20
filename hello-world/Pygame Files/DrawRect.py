import pygame, sys
down = False
clock = pygame.time.Clock()
y = 100
pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0))
d = 100
i = 50
pygame.key.set_repeat(d,i)

while 1:
    clock.tick(30)
    pygame.draw.rect(screen, (0,0,0),(200,0,200,1000),0)
    rect = pygame.draw.rect(screen, (255, 255, 255), (150,y,40,30), 0)
    screen.blit(screen, rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y-5
            elif event.key == pygame.K_DOWN:
                y = y+5
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            down = False
        elif event.type == pygame.MOUSEMOTION:
            if down:
                rect.center = event.pos
            