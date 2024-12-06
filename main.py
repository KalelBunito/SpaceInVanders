import pygame, sys
import random
from player import Player
from enemy import Enemy

pygame.init()

# Configuraçoes iniciasis de tela
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Player Game")

player = Player(370, 500, 50)
bullets = []

inimigos = []



while True:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()  # Tempo atual do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # VERIFICAR SE AS TECLAS FORAM PRESSIONADAS
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
            bullets.append(player.shoot())
            last_shot = current_time

    if keys[pygame.K_LEFT]:
            player.move_left()

    if keys[pygame.K_RIGHT]:
            player.move_right()
            
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)

        if bullet.y < -bullet.size:
            bullets.remove(bullet)

    player.draw(screen)
    enemy.draw(screen)
    pygame.display.update()