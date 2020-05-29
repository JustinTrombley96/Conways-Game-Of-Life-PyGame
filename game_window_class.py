import pygame
from cell_class import *
vec = pygame.math.Vector2

class Game_window:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x,y)
        self.width, self.height = 800, 800
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()


    def draw(self):
        self.image.fill((100, 100, 100))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))