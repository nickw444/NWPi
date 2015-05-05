
# Simple class to return a sprite from a rectangle that is sent to it.

import pygame
from noticer import *
from constants import *

class spriteFromRect(pygame.sprite.Sprite):
	def __init__(self, dimensions):                     # initialise method
        pygame.sprite.Sprite.__init__(self)
     