import pygame, sys
from player import Player

pygame.init()

# Configuraçoes iniciasis de tela
screen = pygame.display.set_mode((800,600))
screen.fill((0, 0, 0))
pygame.display.set_caption("Player Game")

player = Player(370, 500, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

player.draw(screen)
pygame.display.update.update()