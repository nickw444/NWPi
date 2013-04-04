#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# Main UIView Class. Made for subclassing for other Views and ANY other object
# This is probably the most heavily used class throughout the library, and still needs much work
# However, the nature of the class allows easy modification and cool new things to be added

import pygame
from noticer import *
from constants import *
import Images

class UIView():
    def __init__(self, dimensions, parent, background=(255,255,255), borders=(0, 0, 0, 0), borderColor=(0, 0, 0)):
        self.image = pygame.Surface(dimensions)                 # Make a image/canvas to draw things to.
        self.image.fill(background)                             # Fill the image with the specified borderColor 
        self.rect = pygame.Rect((0, 0), dimensions)             # Initialise a rectangle at x=0 and y=0, add coordinates
        self.subViews = []                                      # Initialise subViews array (should be empty)
        self.isVisible = True                                   # Set the visible flag to true
        self.parent = parent                                    # Set the parent for later traversal use
        self.backgroundcolor = background                       # Set the background color for later use/painting
        self.borderColor = borderColor                          # Same with the border color for later painting
        self.borders = borders                                  # Annnnd, the border widths for each side (yes, i stole this from the CSS2 way of doing borders... (top, right, bottom, left))
        self.customInitial()                                    # Run the custom initialisation method (legacy tbh), I should have instead just allowed subClasses to run UIView.__init__. Will fix in the future
        self.updateView()                                       # Update the overall UIView and win.

    def addSubView(self, subView):
        # Add a subView to the view. Good to add more UIViews below this one, or other objects such as UIButtons.
        self.subViews.append(subView)               # Add the subView to the array
        self.updateView()                           # Update this view.

    def setOpacity(self, opacity):
        self.image.set_alpha(opacity)               # Set the opacity of this view
        self.updateView()                           # Re-paint/fill accordingly.

    def customInitial(self):
        # Method for subclassing as the custom initilization method
        pass

    def clearSubviews(self):
        self.subViews = []                          # Remove ALL subviews from this vieww
        self.updateView()                           # Tell this view to update, should re-paint the fact it has no subViews

    def addBorders(self, borders = False):
        # Method to draw borders to the UIView. Pretty simple, just geometry and a bit of math. I'm not going to explain this one.
        if borders != False:
            self.borders = borders
        self.image.fill(self.borderColor, ((0, 0),(self.rect.width, self.borders[0])))
        self.image.fill(self.borderColor, ((self.rect.width - self.borders[1], 0),(self.borders[1], self.rect.height)))
        self.image.fill(self.borderColor, ((0, self.rect.height - self.borders[2]),(self.rect.width, self.borders[2])))
        self.image.fill(self.borderColor, ((0, 0),(self.borders[3], self.rect.height)))

    def setCustomCallback(self, callback):
        # Allows setting of a callback on a button.
        self.actions = callback

    def setBackgroundImage(self, image):
        self.image, self.rect = Images.load_image(image)

    def userCallback(self, event, caller, withinBounds):
        # Method to run the users custom callback. This will catch fatal exceptions (luckily)
        try:
            self.actions(self, event, caller, withinBounds)
            # Method exists, and was used.
        except (AttributeError, TypeError):
            # Method does not exist.  What now?
            noticer("Method self.actions() does not exist", 2, self)

    def updateView(self):
        # print self.subViews
        # Blitting method for viewController.
        self.image.fill(self.backgroundcolor)                     # Re-Fill the canvas, wipe EVERYTHING
        self.addBorders()
        for subView in self.subViews:                              # Loop through each SubView
            self.image.blit(subView.image, subView.rect)               # Blit the subView to the canvas
        self.parent.updateView()                     # Tell the navigationcontroller that it needs to be updated (It'll just blit this views canvas to itself). If there are nested UIViews, it'll just go up, and up, and up until it reaches the topmost object

    def manageEvent(self, event, caller, withinBounds=True):
    # Traversing down the events tree. We receieved an event from the parent NavigationViewController.
    # We need to now pass this even down the tree to the corresponding object that the mouse landed on or whatnot.
        # print "Found a subUIView"
        if withinBounds:
            self.userCallback(event, caller, withinBounds)
        for subView in self.subViews:                                                       # Loop Through each SubView that is LISTENING for events.
            if self.isVisible:                                                                      # Ensure this view is visible (It should be if we've already come this far)
                outside = False                                                                     # Some pre-variable for later reference
                mouse = (event.pos[0] - self.rect.x, event.pos[1] - self.rect.y)                    # Get the mouse Position
                if mouse[0] > subView.rect.topleft[0]:                                                  # Check the mouse position in regards to the subView's rectangle.
                    if mouse[1] > subView.rect.topleft[1]:
                        if mouse[0] < subView.rect.bottomright[0]:
                            if mouse[1] < subView.rect.bottomright[1]:                                      # Mouse is within the bounds                           
                                # It's easier to ask forgiveness than to ask permission.                    # Catching exceptions is key here, in case the subView doesn't have a callback method implemented
                                try:
                                    subView.manageEvent(event, self, True)                                  # Method exists, and was used.                                   
                                except (AttributeError, TypeError):
                                    noticer("Method manageEvent() does not exist", 1, subView)              # Method does not exist.  What now?
                            else:
                                outside = True                                     # Move back down the tree, setting the outside variable to True if the mouse is outside.
                        else:
                            outside = True
                    else:
                        outside = True
                else:
                    outside = True

                if outside == True:     # Mouse is outside, Try send the callback method again, except with the parameter inside = False (This fixes mousebuttonups)
                    try:
                        subView.manageEvent(event, self, False)
                    except (AttributeError, TypeError):
                        noticer("Method manageEvent(ddd) does not exist", 1, subView)

