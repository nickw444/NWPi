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
                # self.parent.parent.removeSubView(self.parent.parent.gameView)
                self.parent.parent.removeSubView(self.parent)
                print "MEEEE" + str(self.parent)
                print "SUBVIEWSSS: " + str(self.parent.parent.subViews)
                self.parent.parent.gameView.isVisible = True
                for view in self.parent.parent.subViews:
                    view.isVisible = True
                # self.parent.updateView()
                # self.parent.parent.parent.parent.parent.removeSubView(self.parent)
            
        okayButton = UIButton((70,30), self)
        okayButton.setText("Okay")
        okayButton.actions = hideView
        okayButton.rect.x = self.rect.width - okayButton.rect.width - 10
        okayButton.rect.y = self.rect.height - okayButton.rect.height - 10
        self.addSubView(okayButton)

        for view in self.parent.subViews:
            if view != self:
                view.isVisible = False