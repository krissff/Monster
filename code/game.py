#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Const import WIN_WIDHT, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return =  menu.run()

            if menu_return == MENU_OPTION [0]:
                level = Level(self.window, 'LevelPb', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION [2]:
                pygame.quit()
                quit()
            else:
                pass









