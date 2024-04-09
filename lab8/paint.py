import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

#fps
pygame.time.Clock().tick(120)

#colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

x, y, x2, y2 = -1, -1, -1, -1

screen = pygame.display.set_mode((1200, 800))
mini_scr = pygame.Surface(screen.get_size())
drawing_ins = pygame.Surface((295, 50))

pygame.draw.rect(drawing_ins, RED, (145, 5, 40, 40))
pygame.draw.rect(drawing_ins, GREEN, (195, 5, 40, 40))
pygame.draw.rect(drawing_ins, BLUE, (245, 5, 40, 40))
pygame.draw.rect(drawing_ins, WHITE, (105, 5, 30, 40), width=0)
pygame.draw.rect(drawing_ins, RED, (105, 5, 30, 15))
pygame.draw.rect(drawing_ins, WHITE, (5, 5, 40, 40), width=3)
pygame.draw.circle(drawing_ins, WHITE, (75, 25), radius=20, width=3)


def draw_circle(screen):
    pygame.draw.circle(screen, colors[current_color], (x,y), radius=((x2-x)**2+(y2-y)**2)**0.5, width=3)

def eraser(screen):
    pygame.draw.circle(mini_scr, (0, 0, 0), (x2, y2), radius=10)

def draw_rect(screen):
    x_local, y_local = x, y
    width, height = x2-x, y2-y
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2
        height = y - y2

    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, height), width=3)

colors = {"red":RED, "green":GREEN, "blue":BLUE}
current_color = 'red'
modes = {'circle':draw_circle, 'eraser':eraser, 'rect':draw_rect}
current_mode = 'rect'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 145 <= x <= 285 and 755 <= y <= 800:
                if x<190:
                    current_color = 'red'
                elif x<240:
                    current_color = 'green'
                else:
                    current_color = 'blue'
            elif 0 <= x <= 145 and 755 <= y <= 800:
                if x<50:
                    current_mode = 'rect'
                elif x<100:
                    current_mode = 'circle'
                else:
                    current_mode = 'eraser'

            x2, y2 = x, y
        if pygame.mouse.get_pressed()[0]:
            x2, y2 = pygame.mouse.get_pos()
            screen.blit(mini_scr, (0, 0))
            modes[current_mode](screen)
            screen.blit(drawing_ins, (0, 750))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            modes[current_mode](mini_scr)
    screen.blit(drawing_ins, (0, 750))
    pygame.display.flip()

    pygame.display.update()
    pygame.time.Clock().tick(120)