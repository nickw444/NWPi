#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# Basic class for creating text. Will take preferences from constants class.
from constants import *


class textObject():
    def __init__(self, text="", font=False, shadowActive=False, color=(35, 35, 35), shadowColor=(255, 255, 255)):
        cont = constants()                                      # Grab the constants
        if font == False:                                       # check if the font is defined
            font = cont.defaultFont                                 # if font is undefined, go grab the font from the constants instead
        if shadowActive:                                        # check if the user wanted shadow
            self.image = font.render(text, 1, shadowColor)          # if they did, render the shadow first,
            self.image.blit(font.render(text, 1, color), (0, -1))   # then render the text on top, -1 pixels on the y axis
        else:
            self.image = font.render(text, 1, color)                # User didn't want shadow, simply render text
        self.rect = self.image.get_rect()                       # set the objects rectangle for centering and placing on a viewController.
