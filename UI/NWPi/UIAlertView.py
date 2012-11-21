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
from UIView import * 
from UIButton import *

class UIAlertView(UIView):
    def customInitial(self):
        def hideView(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                self.parent.parent.removeSubView(self.parent)
            
        okayButton = UIButton((70,30), self)
        okayButton.setText("Okay")
        okayButton.actions = hideView
        okayButton.y = 50
        okayButton.x = 50
        self.addSubView(okayButton)