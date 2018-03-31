#!/usr/bin/env python3.6
"""
Can change during game
"""

import pygame
from global_vars import *

# Sprites lists
all_sprites_list = pygame.sprite.Group()

# Player default start position
PLAYER_START_POS_X = SCREEN_WIDTH - 70 # (SCREEN_WIDTH / 2) - 35
PLAYER_START_POS_Y = SCREEN_HEIGHT - 150 # SCREEN_HEIGHT - (70 * 2)

# Player characteristics
PLAYER_STARTING_LIVES = 3 

# Game conditions
LEVEL = 1
LOOSE = False

