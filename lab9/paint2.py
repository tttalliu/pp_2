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
toolbar = pygame.Surface((500, 50))

pygame.draw.rect(toolbar, WHITE, (10, 5, 30, 40), width=3)
pygame.draw.circle(toolbar, WHITE, (75, 25), radius=20, width=3)
pygame.draw.rect(toolbar, WHITE, (105, 5, 30, 40), width=0)
pygame.draw.rect(toolbar, (200, 0, 0), (105, 5, 30, 15))
pygame.draw.polygon(toolbar, WHITE, [(195, 45), (190 + 45, 45), (195, 5)])
pygame.draw.rect(toolbar, RED, (345, 5, 40, 40))
pygame.draw.rect(toolbar, GREEN, (395, 5, 40, 40))
pygame.draw.rect(toolbar, BLUE, (445, 5, 40, 40))
pygame.draw.rect(toolbar, WHITE, (145, 5, 40, 40), width=3)
pygame.draw.polygon(toolbar, WHITE, [(250, 45), (265, 5), (285, 45)])
pygame.draw.polygon(toolbar, WHITE, [(290, 25), (315, 5), (340, 25), (315, 45)])


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

def draw_square(screen):
    x_local, y_local = x, y
    width = x2 - x
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2

    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, width), width=3)

def draw_eq_tr(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2 - 50, y2 + 50), (x2, y2), (x2 + 50, y2 + 50)])

def draw_right_tr(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2, y2), (x2 + 50, y2), (x2, y2 - 50)])

def draw_rhombus(screen):
    pygame.draw.polygon(screen, colors[current_color], [(x2 - 30, y2 + 20), (x2, y2), (x2 + 30, y2 + 20), (x2, y2 + 40)])

colors = {"red":RED, "green":GREEN, "blue":BLUE}
current_color = 'red'
modes = {"circle": draw_circle, "eraser": eraser, "rect": draw_rect, "square": draw_square, "eq_tr": draw_eq_tr, "right_tr": draw_right_tr, "rhombus": draw_rhombus}
current_mode = 'rect'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 0 <= x <= 500 and 755 <= y <= 800:
                if x < 50:
                    current_mode = 'rect'
                elif x < 100:
                    current_mode = 'circle'
                elif x < 150:
                    current_mode = 'eraser'
                elif x < 195:
                    current_mode = 'square'
                elif x < 245:
                    current_mode = 'eq_tr'
                elif x < 290:
                    current_mode = 'right_tr'
                elif x < 340:
                    current_mode = 'rhombus'
                elif x < 390:
                    current_color = 'red'
                elif x < 440:
                    current_color = 'green'
                else:
                    current_color = 'blue'

            x2, y2 = x, y
        if pygame.mouse.get_pressed()[0]:
            x2, y2 = pygame.mouse.get_pos()
            screen.blit(mini_scr, (0, 0))
            modes[current_mode](screen)
            screen.blit(toolbar, (0, 750))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            modes[current_mode](mini_scr)
    screen.blit(toolbar, (0, 750))
    pygame.display.flip()

    pygame.display.update()
    pygame.time.Clock().tick(120)
