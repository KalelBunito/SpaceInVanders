import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.image = pygame.image.load('PlayerSpace.png')
        self.image = pygame. transform.scale(self.image, (size, size))
        self.size = 20
        self.speed = 2

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    def move_right(self):
        if self.x < 800 - self.size:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image,  (self.x, self.y))