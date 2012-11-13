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
    def __init__(self, dimensions, parent, background=(255,255,255), borders=(0, 0, 0, 0), borderColor=(0, 0, 0)):
        self.image = pygame.Surface(dimensions)
        self.image.fill(background)
        self.rect = pygame.Rect((0, 0), dimensions)
        self.subViews = []
        self.isVisible = True
        self.parent = parent
        self.backgroundcolor = background
        self.borderColor = borderColor
        self.borders = borders
        # parent.updateView()

    def addSubView(self, subView):
        print "ADDING SUBVIEW"
        self.subViews.append(subView)
        self.updateView()

    def addBorders(self, borders = False):
        if borders != False:
            self.borders = borders
        self.image.fill(self.borderColor, ((0, 0),(self.rect.width, self.borders[0])))
        self.image.fill(self.borderColor, ((self.rect.width - self.borders[1], 0),(self.borders[1], self.rect.height)))
        self.image.fill(self.borderColor, ((0, self.rect.height - self.borders[2]),(self.rect.width, self.borders[2])))
        self.image.fill(self.borderColor, ((0, 0),(self.borders[3], self.rect.height)))
        # self.image.fill(self.borderColor, ((0, self.rect.height - self.borders[2]),(self.rect.width, self.borders[2])))

    def setCustomCallback(self, callback):
        # Allows setting of a callback on a button.
        self.actions = callback

    def userCallback(self, event, caller):
        # Method to run the users custom callback. This will catch fatal exceptions (luckily)

        # self.actions = showViewOne
        try:
            self.actions(self, event, caller)
            # Method exists, and was used.
        except (AttributeError, TypeError):
            # Method does not exist.  What now?
            noticer("Method self.actions() ddd does not exist", 2, self)

    def updateView(self):
        print self.subViews
        # Blitting method for viewController.
        self.image.fill(self.backgroundcolor)                     # Re-Fill the canvas, wipe EVERYTHING
        self.addBorders()
        for subView in self.subViews:                              # Loop through each SubView
            self.image.blit(subView.image, subView.rect)               # Blit the subView to the canvas
        # self.screen.blit(self.canvas, (0, 0))
        self.parent.updateView()                     # Tell the navigationcontroller that it needs to be updated (It'll just blit this views canvas to itself)

    def subTest(self, event, caller, withinBounds):
        # print ("COCKS on sub-object" + str(self))
        self.actions(self, event, caller, withinBounds)

    def manageEvent(self, event, caller, withinBounds=True):
    # Traversing down the events tree. We receieved an event from the parent NavigationViewController.
    # We need to now pass this even down the tree to the corresponding object that the mouse landed on or whatnot.
        if withinBounds:
            # self.userCallback(event, caller)
            # self.actions()
            print ("COCKS on object" + str(self))
        for subView in self.subViews:                                                       # Loop Through each SubView that is LISTENING for events.
            if self.isVisible:                                                                      # Ensure this view is visible (It should be if we've already come this far)
                outside = False                                                                     # Some pre-variable for later reference
                mouse = event.pos                                                                       # Get the mouse Position
                if mouse[0] > subView.rect.topleft[0]:                                                  # Check the mouse position in regards to the subView's rectangle.
                    if mouse[1] > subView.rect.topleft[1]:
                        if mouse[0] < subView.rect.bottomright[0]:
                            if mouse[1] < subView.rect.bottomright[1]:
                                # noticer("Mouse within bounds", 0, subView)                                  # Mouse is within the bounds
                                # It's easier to ask forgiveness than to ask permission.                    # Catching exceptions is key here, in case the subView doesn't have a callback method implemented
                                try:
                                    print("Calling the subView")
                                    subView.subTest(event, self, True)
                                    # subView.manageEvent(event, self, True)                                      # Method exists, and was used.
                                except (AttributeError, TypeError):
                                    noticer("Method manageEvent() does not exist", 1, subView)                  # Method does not exist.  What now?
                            else:
                                outside = True                                                       # Move back down the tree, setting the outside variable to True if the mouse is outside.
                        else:
                            outside = True
                    else:
                        outside = True
                else:
                    outside = True

                if outside == True:                                                                 # Mouse is outside, Try send the callback method again, except with the parameter inside = False (This fixes mousebuttonups)
                    try:
                        subView.manageEvent(event, self, False)
                    except (AttributeError, TypeError):
                        noticer("Method manageEvent(ddd) does not exist", 1, subView)

