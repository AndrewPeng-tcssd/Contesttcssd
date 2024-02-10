import pygame
import random


class Platform:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = random.randint(0, 930 - self.width)
        self.y = random.randint(350, 635)
        self.sprite = pygame.Rect(self.x, self.y, self.width, self.height)  # main platform
        self.up = pygame.Rect(self.x, self.y - 2, self.width, self.height / 5)  # the upper rectangle for hit boxes
        self.bottom = pygame.Rect(self.x, self.y + 18, self.width, self.height / 10)  # the bottom rectangle for hit boxes
        self.left = pygame.Rect(self.x, self.y, self.width / 30, self.height)  # the left rectangle for hit boxes
        self.right = pygame.Rect(self.x + 98, self.y, self.width / 30, self.height)  # the right rectangle for hit boxes

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.sprite)
        # pygame.draw.rect(window, (255, 0, 0), self.up) 
        # pygame.draw.rect(window, (255, 0, 0), self.bottom)
        # pygame.draw.rect(window, (255, 0, 0), self.left)
        # pygame.draw.rect(window, (255, 0, 0), self.right)
