import pygame

class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.image = pygame.image.load('PlayerSpace.png')
        self.image = pygame. transform.scale(self.image, (size, size))
        self.size = size
        self.speed = 2

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    def move_right(self):
        if self.x < 800 - self.size:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image,  (self.x, self.y))
    
    def shoot(self):
        return Bullet(self.x + self.size // 2 - 2, self.y, 5)

class Bullet:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 0, 0)
        self.speed = -2

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size * 2))
