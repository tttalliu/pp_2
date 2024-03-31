import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Music Player")

bg_image = pygame.image.load("player.png").convert()

font = pygame.font.SysFont("Arial", 24)

pygame.mixer.init()

music_files = ["mrs_magic.mp3", "cologne.mp3"]
current_track_index = 0

pygame.mixer.music.load(music_files[current_track_index])


def player():
    screen.blit(bg_image, (0, 0))


def play_music():
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()


def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()


def draw_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()

    player()

    draw_text(f"Track: {current_track_index + 1}/{len(music_files)}", 125, 50)

    draw_text("Space: Play", 125, 100)
    draw_text("S: Stop", 125, 150)
    draw_text("Right: Next", 240, 100)
    draw_text("Left: Prev", 240, 150)

    pygame.display.flip()

pygame.quit()
sys.exit()
