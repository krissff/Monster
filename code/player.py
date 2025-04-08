#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDHT, PLAYER_KEY_SHOTS
from code.PlayerShot import PlayerShot
from code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDHT:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_SHOTS[self.name]]:
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))