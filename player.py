
import pygame
import random
from all_graphics import  garry, WIDTH, HEIGHT, piu


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = garry
        self.image = pygame.transform.scale(garry, (110, 65))
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, HEIGHT / 2)
        self.speedy = 0
        self.speedx = 0
        self.hp = 100

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -8
            self.image = pygame.transform.scale(garry, (110, 65))
        if keystate[pygame.K_s]:
            self.speedy = 8
            self.image = pygame.transform.scale(garry, (110, 65))
        if keystate[pygame.K_a]:
            self.speedx = -8
            self.image = pygame.transform.scale(garry, (110, 65))
        if keystate[pygame.K_d]:
            self.speedx = 8
            self.image = pygame.transform.scale(garry, (110, 65))
        if keystate[pygame.K_w] and keystate[pygame.K_d]:
            self.image = pygame.transform.scale(garry, (110, 65))
            self.image = pygame.transform.rotate(self.image, 45)
        if keystate[pygame.K_s] and keystate[pygame.K_d]:
            self.image = pygame.transform.scale(garry, (110, 65))
            self.image = pygame.transform.rotate(self.image, -45)

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(piu)
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = -20
        self.speedy = -20

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()