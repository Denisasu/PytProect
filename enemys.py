import pygame
import random

from all_graphics import WIDTH, HEIGHT, clans, sova, dementor, pojirateli

class Clans(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(clans)
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(WIDTH)
        self.rect.x = random.randrange(WIDTH, WIDTH + 100)
        self.speedx = random.randrange(3, 5)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.y = random.randrange(WIDTH)
            self.rect.x = random.randrange(WIDTH, WIDTH + 100)
            self.speedx = random.randrange(3, 5)


class Sova(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(sova)
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(WIDTH)
        self.rect.x = random.randrange(WIDTH, WIDTH + 100)
        self.speedx = random.randrange(2, 4)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.y = random.randrange(WIDTH)
            self.rect.x = random.randrange(WIDTH, WIDTH + 100)
            self.speedx = random.randrange(2, 4)


class Dementor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dementor
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(WIDTH)
        self.rect.x = random.randrange(WIDTH, WIDTH + 100)
        self.speedx = random.randrange(6, 8)
        self.speedy = random.randrange(-4, 4)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0:
            self.rect.y = random.randrange(WIDTH)
            self.rect.x = random.randrange(WIDTH, WIDTH + 100)
            self.speedx = random.randrange(6, 8)
            self.speedy = random.randrange(-4, 4)


class Pojirateli(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(pojirateli)
        self.image.set_colorkey("white")
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(WIDTH)
        self.rect.x = random.randrange(WIDTH, WIDTH + 100)
        self.speedx = random.randrange(5, 7)
        self.speedy = random.randrange(-2, 2)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.rect.right < 0:
            self.rect.y = random.randrange(WIDTH)
            self.rect.x = random.randrange(WIDTH, WIDTH + 100)
            self.speedx = random.randrange(5, 7)
            self.speedy = random.randrange(-2, 5)
