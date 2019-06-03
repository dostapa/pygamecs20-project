#imports
import pygame
import random
import time
import sys
#classes for the sprites
class enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
pygame.init()
pygame.display.set_caption('game')

#screen height and width
screenw = 800
screenh = 800

#sets the screen to the screen variable and defines the screen width and height.
screen = pygame.display.set_mode((screenw, screenh))
done = False

#Defines the clock(Frames Per Second)
clock = pygame.time.Clock()
#defines the sprite classes to a sprite variable and creates their groups
playerg = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy1 = enemy1()
player = player()
bullet = bullet()
enemies.add(enemy1)
playerg.add(player)
bullets.add(bullet)

backgroundcolor = (80,0,40)
#variables
php = (0,255,0)
phw = 100
bx = 0
by = 0
enemycount = 3
#Main game loop
while player.rect.x != enemy1.rect.x:
    if player.rect.x > enemy1.rect.x:
        enemy1.rect.x += 1
    if player.rect.y > enemy1.rect.y:
        enemy1.rect.y -= 1
while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    bx, by = event.pos
                    bullet.rect.x = bx
                    bullet.rect.y = by
                    print(bx,by)

        #Listens to the keyboard for specific key presses, then runs the if statement that is true
        pressed = pygame.key.get_pressed()
        #events
        if pressed[pygame.K_w]:
            player.rect.y -= 2

        if pressed[pygame.K_s]:
            player.rect.y += 2

        if pressed[pygame.K_a]:
            player.rect.x -= 2

        if pressed[pygame.K_d]:
            player.rect.x += 2

        if pygame.sprite.collide_rect(player,enemy1):
            phw -= 1.5

        if pygame.sprite.collide_rect(bullet,enemy1):
                pygame.sprite.Sprite.kill(enemy1)
                enemycount -= 1;

        if phw <= 0:
            sys.exit()
        #updates the sprite groups
        bullets.update()
        enemies.update()
        playerg.update()
        #Fills the screen every time the screen is updated (makes it so the square doesn't leave a ghost behind)

        screen.fill(backgroundcolor)
        #draws healthbar for player

        pygame.draw.rect(screen, php, pygame.Rect(40, 20, phw, 20))
        #draws the sprites on the screen

        bullets.draw(screen)
        enemies.draw(screen)
        playerg.draw(screen)
        #Causes the screen to show.
        pygame.display.flip()
        #fps
        clock.tick(60)
