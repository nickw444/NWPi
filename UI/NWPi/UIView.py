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

class UIView():
    def __init__(self, dimensions, parent, background=(255,255,255)):
        self.image = pygame.Surface(dimensions)
        self.image.fill(background)
        self.rect = pygame.Rect((0, 0), dimensions)
        self.subViews = []
        self.parent = parent
        self.backgroundcolor = background
        # parent.updateView()

    def addSubView(self, subView):
        print "ADDING SUBVIEW"
        self.subViews.append(subView)

    def updateView(self):
        print self.subViews
        # Blitting method for viewController.
        self.image.fill(self.backgroundcolor)                     # Re-Fill the canvas, wipe EVERYTHING
        for subView in self.subViews:                              # Loop through each SubView
            self.image.blit(subView.image, subView.rect)               # Blit the subView to the canvas
        # self.screen.blit(self.canvas, (0, 0))
        self.parent.updateView()                     # Tell the navigationcontroller that it needs to be updated (It'll just blit this views canvas to itself)
