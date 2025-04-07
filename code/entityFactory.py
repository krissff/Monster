#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Const import WIN_WIDHT, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'LevelPb':
                list_pb = []
                for i in range(5):
                    list_pb.append(Background(f'LevelPb{i}', (0, 0)))
                    list_pb.append(Background(f'LevelPb{i}', (WIN_WIDHT, 0)))

                return list_pb
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDHT + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDHT + 10, random.randint(40, WIN_HEIGHT - 40)))

