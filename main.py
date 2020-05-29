import pygame
import sys
from game_window_class import *

width, height = 1000, 1000
background = (50, 50, 200)
FPS = 60

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def update():
    game_window.update()
def draw():
    game_window.draw()
    window.fill(background)

pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_window = Game_window(window, x, y)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()