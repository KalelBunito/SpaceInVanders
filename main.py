import pygame, sys
from player import Player

pygame.init()

# Configuraçoes iniciasis de tela
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Player Game")

player = Player(370, 500, 50)
bullets = []

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # VERIFICAR SE AS TECLAS FORAM PRESSIONADAS
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bullets.append(player.shoot())

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move_left()

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move_right()
            
            for bullet in bullets[:]:
                bullet.move()
                bullet.draw(screen)

                if bullet.y < -bullet.size:
                    bullets.remove

    player.draw(screen)
    pygame.display.update()