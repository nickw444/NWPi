#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# FancyButton Subclass from UIButton
# Just a custom font, and some offset.
# Easy as Pi

from constants import *
from UIButton import *


class fancyButton(UIButton):
    def __init__(self):
        UIButton.__init__(self, (160, 60))      # Initialise the UIButton
        cont = constants()                      # Grab the constants
        self.font = cont.fancyButtonFont        # Change the font for this button
        self.textOffset = (0, 5)                # Add an offset because the stupid font is a dick
