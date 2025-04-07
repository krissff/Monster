#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDHT
from code.entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centerx -= 1
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDHT

        pass
