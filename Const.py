# Tamanho da tela de fundo
import pygame

WIN_WIDHT = 480
WIN_HEIGHT = 270

#Cores
COLOR_PURPLE = 128, 0, 128
COLOR_WHITE = 255, 255, 255
COLOR_YELLOW = 255, 255, 0

#Opções do Menu
MENU_OPTION = ('New Game',
               'Score',
               'Exit')

# Velocidade das Imagens
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'LevelPb0': 0,
    'LevelPb1': 1,
    'LevelPb2': 2,
    'LevelPb3': 3,
    'LevelPb4': 4,
    'Player': 4,
    'PlayerShot': 6,
    'Enemy1': 4,
    'Enemy2': 5,
}

#S
SPAWN_TIME = 4000

#Vidas
ENTITY_HEALTH = {
    'LevelPb0': 999,
    'LevelPb1': 999,
    'LevelPb2': 999,
    'LevelPb3': 999,
    'LevelPb4': 999,
    'Player': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}

#Tiros
PLAYER_KEY_SHOTS = {'Player': pygame.K_RCTRL}