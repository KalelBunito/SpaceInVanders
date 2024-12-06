import pygame

class Enemy:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.image = pygame.image.load('enemy.jpeg')
        self.image = pygame. transform.scale(self.image, (size, 40))

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image,  (self.x, self.y))