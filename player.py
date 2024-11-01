import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.image = pygame.image.load('PlayerSpace.png')
        self.image = pygame. transform.scale(self.image, (size, size))

    def draw(self, screen):
        screen.blit(self.image(self.x, self.y))