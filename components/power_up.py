import pygame
import random

from utils.constants import (
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR
)

from os import path
allowed_speed = list(range(3, 7))
class Power(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.image = pygame.image.load(path.join(IMG_DIR, "powerup stone.png")).convert()
        self.image = pygame.transform.scale(self.image, (50 // size, 50 // size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_HEIGHT - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.speedy = random.choice(allowed_speed)
        self.speedx = 0
        self.size = size


    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
