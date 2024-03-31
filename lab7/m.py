import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 706), pygame.RESIZABLE)

bg_image = pygame.image.load("clock.png").convert()

minute_hand_image=pygame.image.load("right_hand.png").convert_alpha()
second_hand_image=pygame.image.load("left_hand.png").convert_alpha()

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)

def mickey_clock():
    screen.blit(bg_image, (0, 0))

    current_time = pygame.time.get_ticks() // 1000 
    minute = current_time % 3600 // 60
    second = current_time % 60

    minute_angle = -(minute * 6) + 90 
    second_angle = -(second * 6) + 90

    minute_hand_rotated, minute_hand_rect = rot_center(minute_hand_image, minute_angle, 700 // 2, 706 // 2)
    screen.blit(minute_hand_rotated, minute_hand_rect)

    second_hand_rotated, second_hand_rect = rot_center(second_hand_image, second_angle, 700 // 2, 706 // 2)
    screen.blit(second_hand_rotated, second_hand_rect)

    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mickey_clock()

    pygame.time.Clock().tick(60)

pygame.quit()