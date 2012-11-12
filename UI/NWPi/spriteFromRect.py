#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# Main UIButton Class. Made for subclassing for other buttons
# Whole button is being drawn with code, no images in sight! Woo!
import pygame
from noticer import *
from constants import *

class spriteFromRect(pygame.sprite.Sprite):
	def __init__(self, dimensions):                     # initialise method
        pygame.sprite.Sprite.__init__(self)
        cont = constants()                              # Grab the constants
     