import pygame
from utils.constants import (
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR
)

from components.bullet import Bullet
from os import path


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR,"alien.png"))
        self.image =pygame.transform.scale(self.image, (50, 50 ))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.movement_on_x = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.movement_on_x
        if key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.movement_on_x

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 0, -5)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def powerup(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 0, -5)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)
        bullet = Bullet(self.rect.centerx, self.rect.top,-5, -5)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)
        bullet = Bullet(self.rect.centerx, self.rect.top, 5, -5)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)
