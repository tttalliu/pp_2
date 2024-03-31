import pygame
import sys

pygame.init()

W=500
H=300

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius=25
diameter=radius*2

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

ball_x = (W-diameter) // 2
ball_y = (H-diameter) // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            W,H=event.size
            screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
            ball_x = max(0, min(ball_x, W-diameter))
            ball_y = max(0, min(ball_y, H-diameter))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(0, ball_y - 20)
    if keys[pygame.K_DOWN]:
        ball_y = min(H-diameter, ball_y + 20)
    if keys[pygame.K_LEFT]:
        ball_x = max(0, ball_x - 20)
    if keys[pygame.K_RIGHT]:
        ball_x = min(W-diameter, ball_x + 20)

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x + radius, ball_y + radius),radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
