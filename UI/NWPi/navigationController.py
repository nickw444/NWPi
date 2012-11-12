#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# NavigationController Class
# This is the topMost class on the view tree model.
# All subviews MUST be placed on this view by running "AddSubview" method
# It is recomended to only place objects of Viewcontroller class to this object as they can handle events correctly
import pygame               # Grab pygame
import copy                 # Allow for copying of objects (not just object references which kills everything)
from noticer import *       # Allow debugging and logging.


class navigationController():                               # Define the class
    def __init__(self, screen):
        self.subViews = []                                  # Set the subViews Variable to data type of list
        self.backgroundcolor = (50, 50, 50)                 # Set the self background color
        self.screen = screen                                # Save the screen object reference for later blitting (as this is the topmost object)
        self.canvas = pygame.Surface(screen.get_size())     # Draw the canvas
        self.updateView()                                   # Update this navigation controller with the new blitted canvas
    def addSubView(self, identifier, object):
        # Method allows the NavigationController to have subViews added.
        # Will simply add them to the subViews array for use later in the self.updateView method
        # The object being added MUST have a runCallback(event) method otherwise an exception will be thown (CBF catching errors)
        self.subViews.append({"identifier": identifier, "object": object})              # Add to the array
        self.updateView()                                                             # Update this navigation controller and blit everything from below upwards.

    # method removeSubView needs a re-write and CBF right now. Concept is still here, just needs re-writing to account for the different list structure
    # def removeSubView(self, object):
    #     # Method will simply find the object passed and remove it from
    #     self.subViews.remove(object)
    #     self.updateView()

    def updateView(self):
        # this method basically:
        #   1. Wipes the canvas clean
        #   2. Blits each subView to the canvas, in order that they are in in the list AND only if they are Visible (Saves memory this way)
        #   3. Blits the canvas to the screen
        noticer("Updating Navigation Controller", 0, self)
        self.canvas.fill(self.backgroundcolor)
        for subView in self.subViews:
            if subView['object'].isVisible:
                self.canvas.blit(subView['object'].canvas, (0, 0))
        self.screen.blit(self.canvas, (0, 0))

    def makeKeyAndVisible(self, identifier):
        # This method is needed to bring a subView/viewController to the font. It re-organises the subViews list.
        i = 0                                                       # Set a counter for the loop
        found = False                                               # Set some defaults
        views = copy.copy(self.subViews)                            # Make a copy of the subViews array so we can modify it without fucking everything up
        while i < len(views):                                       # Loopy
            if (views[i]['identifier'] == identifier):                  # Check if the identifier we're looking for is this object
                obj = self.subViews.pop(i)                                  # Remove the object from the middle/top of the array, and get it
                obj['object'].isVisible = True                              # Tell the subView of the object that it is now visible on screen (fixes issues with listening for events - listening for objects that are not on screen)
                self.subViews.append(obj)                                   # Re-append the object to the end
                found = True                                                # For later use, say that we did find a view
                break                                                       # Break the loop, we found the one we need, no need to do any more finding. Don't work the processor too hard
            else:                                                       # Didnt find the object for the identifier :(
                self.subViews[i]['object'].isVisible = False                # Seeing as this isn't the object we're looking for, let's tell it that no, it's no longer visible
            i += 1                                                      # Loop increment
        if found != True:                                          # Check to see if we did find one
            noticer("The ViewController with identifier" + identifier + " was not found", 2, self)  # Warn the console and log that we didn't find anything
            # Because we did tell everything to disable itself for interactions, we need to give the top level one interactivity again.
            topView = copy.copy(self.subViews)                          # Get the SubViews Array
            top = topView.pop()                                         # Get the last item in the array (The one that is showing)
            top['object'].isVisible = True                              # Tell the object that it is still visible (because we told it earlier that it wasn't)
        self.updateView()                                          # Now that everything is basically over, update this navigationController, with the new arrangement of subViews

    def manageEvent(self, event):
        # This is the topmost even manager method
        subviews = copy.copy(self.subViews)     # Copy so we don't destory the REAL list
        sub = subviews.pop()                    # Get the topMost subView
        if sub['object'].isVisible:             # Check to ensure this subView is visible.
            sub['object'].manageEvent(event)        # Send the action to the visible subview
