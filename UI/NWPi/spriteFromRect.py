#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# Simple class to return a sprite from a rectangle that is sent to it.

import pygame
from noticer import *
from constants import *

class spriteFromRect(pygame.sprite.Sprite):
	def __init__(self, dimensions):                     # initialise method
        pygame.sprite.Sprite.__init__(self)
     