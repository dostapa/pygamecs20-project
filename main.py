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
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (200,200)
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,150))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (5000, 5000)
#initializing pygame
pygame.init()
pygame.font.init()
#sets font type
font = pygame.font.SysFont('Comic Sans MS', 25)
#window caption
pygame.display.set_caption('YEe HaW') 
#sets the screen to the screen variable and defines the screen width and height.
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
done = False
#Defines the clock(Frames Per Second)
clock = pygame.time.Clock()
#defines the sprite classes to a sprite variable and creates their groups
playerg = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#defines sprite variables to their classes
enemy1 = enemy1()
player = player()
bullet = bullet()
#adds sprites to groups to allow for easy rendering
enemies.add(enemy1)
playerg.add(player)
enemies.add(enemy1)
backgroundcolor = (15,15,15)
#variables
phc = (0,255,0)
phh = 150
bx = 0
by = 0
enemycount = 40
level = 0
#random enemy initial spawn
enemy1.rect.x = random.randint(1,1920)
enemy1.rect.y = random.randint(1,1080)
#set cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
#movement rate of the enemy
emoverate = 1
emoverateadd = 0.05

#Main game loop
while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #checks for a click and sets the bullet there
                    bx, by = event.pos
                    bullets.add(bullet)
                    bullet.rect.x = bx
                    bullet.rect.y = by

                elif event.type == pygame.MOUSEBUTTONUP:
                    pygame.sprite.Sprite.kill(bullet)
                    bullet.rect.x = 2000
                    bullet.rect.y = 2000
        #Listens to the keyboard for specific key presses, then runs the if statement that is true
        pressed = pygame.key.get_pressed()
        #events
        if pressed[pygame.K_w]:
            player.rect.y -= 2

        if pressed[pygame.K_s]:
            player.rect.y += 2

        if pressed[pygame.K_a]:
            player.rect.x -= 2

        if pressed[pygame.K_b]:
            level += 1

        if pressed[pygame.K_d]:
            player.rect.x += 2

        if pressed[pygame.K_ESCAPE]:
            done = True

        if pygame.sprite.collide_rect(player,enemy1):
            phh -= 1.5

        #when the player clicks on the enemy
        if pygame.sprite.collide_rect(bullet,enemy1):
                pygame.sprite.Sprite.kill(enemy1)
                enemycount -= 1;
                phh += 2.5

                if enemycount <= 0:
                    level += 1
                    enemycount = 40
                    emoverateadd += 0.02
                    phh += 50

                emoverate += emoverateadd
                enemies.add(enemy1)
                enemy1.rect.x = random.randint(1,1920)
                enemy1.rect.y = random.randint(1,1080)

        if pygame.sprite.collide_rect(bullet,player):
            phh -= 1

        if phh <= 0:
            print("You Lose!")
            done = True

        if player.rect.x != enemy1.rect.x:

            if player.rect.x > enemy1.rect.x:
                enemy1.rect.x += emoverate

            if player.rect.x < enemy1.rect.x:
                enemy1.rect.x -= emoverate

        if player.rect.y != enemy1.rect.y:

            if player.rect.y > enemy1.rect.y:
                enemy1.rect.y += emoverate

            if player.rect.y < enemy1.rect.y:
                enemy1.rect.y -= emoverate

        #updates the sprite groups

        bullets.update()
        enemies.update()
        playerg.update()

        #Fills the screen every time the screen is updated (makes it so the square doesn't leave a ghost behind)

        screen.fill(backgroundcolor)
        #draws healthbar for player

        pygame.draw.rect(screen, phc, pygame.Rect(40, 20, 20, phh))
        #draws the text bars displaying enemy's left and enemy speed

        textsurface = font.render("Enemy's Left: {0}".format(enemycount), False, (255, 255, 255))
        textsurface2 = font.render("Enemy's Speed: {0}".format(emoverate), False, (255, 255, 255))
        textsurface4 = font.render("Level: {0}".format(level), False, (255, 255, 255))

        #draws the text onto the screen

        screen.blit(textsurface,(200,0))
        screen.blit(textsurface2,(200,50))
        screen.blit(textsurface4,(200,100))

        #draws the sprites on the screen

        bullets.draw(screen)
        enemies.draw(screen)
        playerg.draw(screen)

        #Causes the screen to show.

        pygame.display.flip()
        #fps
        clock.tick(60)
