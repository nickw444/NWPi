#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# ViewController Class
# One of the main classes in layout management.
# Can be easily subClassed and new objects can be re-drawn to it in the subclass.
# Simply subclass NWPi.viewController and implement the method "customInitial(self)".
# This will allow you to draw items to the canvas or do funny things with the viewController.
import pygame
from noticer import *
# from Images import *


class viewController():
    def __init__(self, navigationController):
        self.subViews = []                                                  # Set the subViews variable to data type of list
        self.isVisible = False                                              # By default this view will be invisible
        self.backgroundcolor = (230, 230, 230)                              # Set the default background color. Yes, we can change this later on.
        self.navigationController = navigationController                    # Set the parent navigation controller. For use in blitting
        self.screen = navigationController.screen  # for later use yolo     # Grab the screen and reference it
        self.listeningSubViews = []                                         # Set the listeningSubViews array to data type of list
        self.canvas = pygame.Surface(self.screen.get_size())                # initialise the canvas for this view for blitting
        self.customInitial()                                                # Run the custom initialisation method (Yes, it's empty here, but it can be subClasses)
        self.updateView()                                                   # Update this view and all subViews on it.

    def customInitial(self):
        # SubClassable method. This can be edited to allow custom initialisation, such as custom drawing.
        return

    def setBackgroundColor(self, colors):
        # Self explanatory. Set the background color. boom headshot.
        self.backgroundcolor = colors
        self.updateView()

    def manageEvent(self, event):
        # Traversing down the events tree. We receieved an event from the parent NavigationViewController.
        # We need to now pass this even down the tree to the corresponding object that the mouse landed on or whatnot.
        for subView in self.subViews:                                                      # Loop Through each SubView that is LISTENING for events.
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
                                    subView.manageEvent(event, self, True)                                      # Method exists, and was used.
                                except (AttributeError, TypeError):
                                    noticer("Method manageEvent() does not exist when inside", 1, subView)                  # Method does not exist.  What now?
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
                        noticer("Method manageEvent() does not exist when outside", 1, subView)

    def addSubView(self, object, callback=False):
        # This method simply allows subViews to be added to the superView.
        # It also allows them to enable themselves as 'callbackable' if param callback = True
        self.subViews.append(object)                  # Add to the subViews list
        if callback == True:                          # check for callback
            self.listeningSubViews.append(object)       # Callback is enabled, add object to the listeningSubViews list
        self.updateView()                             # Blit all subViews using the updateView method

    def removeSubView(self, object):
        # Remove a view from the superview. Good for removing text or sprites
        self.subViews.remove(object)                        # Simply remove the objects from the array and you're done. Easy as pi.
        self.listeningSubViews.remove(object)               # once again, just remove them from this array too
        self.updateView()                                   # Re-blit everything

    def updateView(self):
        # Blitting method for viewController.
        self.canvas.fill(self.backgroundcolor)                     # Re-Fill the canvas, wipe EVERYTHING
        for subView in self.subViews:                              # Loop through each SubView
            self.canvas.blit(subView.image, subView.rect)               # Blit the subView to the canvas
        # self.screen.blit(self.canvas, (0, 0))
        self.navigationController.updateView()                     # Tell the navigationcontroller that it needs to be updated (It'll just blit this views canvas to itself)
