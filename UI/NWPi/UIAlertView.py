#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# UIAlertView Class, shows a simple and basic window to the user, and will disable any other views on the viewController whilst it is being shown.
# Strictly, this should only be used on a viewController subclass or superclass. Unexpected results may be present if used on a UIView (well, until I subclass ViewController from UIView)
# Objects of these class need a background deleagate class strictly defined. This is a simple UIView, added to the same UIViewController as self.
# This acts as a "faded out" backdrop for maximum user experience.


import pygame
from UIView import * 
from UIButton import *
from textObject import *

class UIAlertView(UIView):
    def customInitial(self):

        # Define the callback to be run when the user clicks the "Okay" button on the window.
        # This will allow a custom callback to be run, but will ALSO remove the UIView from the parent object.
        def hideView(self, event, caller, withinBounds):
            self.parent.okayAction(self,event, caller, withinBounds)                    # Run the custom callback
            if event.type == pygame.MOUSEBUTTONUP:                                      # Ensure this is the mouseup event
                self.parent.parent.removeSubView(self.parent)                               # Remove this view from the parent
                self.parent.parent.removeSubView(self.parent.bgDelegate)                    # We also need to remove the Background delegate from the parent
                for view in self.parent.parent.subViews:                                    # We now need to loop through the subViews of the controller, to set them back to visible
                    view.isVisible = True                                                       # Allow interaction of each subView again!


        okayButton = UIButton((70,30), self)                                            # Initialise a UIButton
        okayButton.setText("Close")                                                     # Give the UIButton some text
        okayButton.actions = hideView                                                   # Give the UIButton the callback - to hide the self object
        okayButton.rect.x = self.rect.width - okayButton.rect.width - 10                # Position the UIButton at the bottom right
        okayButton.rect.y = self.rect.height - okayButton.rect.height - 10
        self.addSubView(okayButton)                                                     # Add the UIButton to the self Object                                              
        
        # Define the default handler for when the hideView method is called
        def okay(self, event, caller, withinBounds):
            pass                                                # Do nothing, as this will be replaced
        self.okayAction = okay                                  # Tell the self object to run the function "okay" when the okay button is pressed

        for view in self.parent.subViews:                       # Because we are showing a UIAlertView, it should be the only clickable object. loop through all of the controllers subviews
            if view != self:                                        # Check if the subview is this view. 
                view.isVisible = False                                     # if it isn't, tell it that it is no longer visible, stopping user interaction with it.
            
    # Basic definition to add text to the UIView. Simply subclasses the textObject class. Easy as pi.
    def setText(self, text):
        textobj = textObject(text)                         
        textobj.rect.centerx = self.rect.width / 2
        textobj.rect.y = 20
        self.addSubView(textobj)

