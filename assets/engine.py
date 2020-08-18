import pygame
import sys


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def infinitebackground(screen, img, y):
    rel_y = y % img.get_height()
    screen.blit(img, (0, rel_y - img.get_height()))
    if rel_y < screen.get_height():
        screen.blit(img, (0, rel_y))
