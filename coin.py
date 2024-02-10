import pygame
import random


class Coin:
    def __init__(self):
        self.x = random.randint(0, 930 - 13)
        self.y = random.randint(350, 650)
        self.width = 13
        self.height = 13
        self.hit_box = pygame.Rect(self.x, self.y, 13, 13)

    def draw(self, window):
        pygame.draw.circle(window, (255, 217, 3), (self.x + self.width / 2, self.y + self.height / 2), self.width / 2)
