#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDHT
from code.background import Background

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


