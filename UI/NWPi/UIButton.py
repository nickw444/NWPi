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
from UIView import *


class UIButton(UIView):
    def __init__(self, dimensions, parent):
        cont = constants() 
        UIView.__init__(self, dimensions, parent)
        self.userText = ""
        self.state = "up"
        self.backgroundcolor = (96, 117, 146)
        self.paint()
        self.font = cont.defaultButtonFont              # set the font, default is the default from constants
        self.textOffset = (0, 0)                        # set the text offset, default there is none
        
        
        
    def setBackgroundColor(self, color):
        self.backgroundcolor = color                    # Set the background color for later painting referenc e
        self.paint()                                    # Paint the object again, this time with the new background
        self.setText()                                  # Re-add the text to the object (yes, paint removed the text :(  ) 

    def setText(self, text=False):
        # This method basically adds text to the object's canvas. Simple really,
        # Simply places it in the center of the button and renders it using the default font, unless specified in the init, or later
        if text != False:
            self.userText = text
        font = self.font
        text1 = font.render(self.userText, 1, (244, 244, 244))
        text1pos = text1.get_rect()
        text1pos.centerx = self.rect.width / 2 + self.textOffset[0]
        text1pos.centery = self.rect.height / 2 + self.textOffset[1]

        font2 = self.font
        text2 = font2.render(self.userText, 1, (10, 10, 10))
        text2pos = text2.get_rect()
        text2pos.centerx = self.rect.width / 2 + self.textOffset[0]
        text2pos.centery = self.rect.height / 2 + 1 + self.textOffset[1]

        self.image.blit(text2, text2pos)
        self.image.blit(text1, text1pos)

    def paint(self):
        self.image = pygame.Surface((self.rect.width, self.rect.height))                            # Fix all the rectangles.  Re-init the image
        if self.state == "down":                                                                    # Paint accordingly whether the mouse is inside or not.
            bg = list(self.backgroundcolor)
            sh = 40                                                 # Shading scale up - Larger the number, the brighter the shaddow
            d = 2                                                   # Shading dithering value, the greater the number, the more dithered colours will be.
            sh2 = [0,0,0]
            self.image.fill((bg[0]/d + sh, bg[1]/d + sh, bg[2]/d + sh), ((1, 1), (self.rect.width - 2, self.rect.height - 2))) # paint the new shadow
        else:                                                       # No shadow needed, paint accordingly, with inset shadow color.
            bg = list(self.backgroundcolor)
            self.image.fill(self.backgroundcolor, ((1, 1), (self.rect.width - 2, self.rect.height - 2)))
            sh = 100

            # Determine the colour of the inset shadow according to the color of the background. Will always have a nice top glow to it.
            if (bg[0] + sh) > 255:
                bg[0] = 255
            else:
                bg[0] += sh
            if (bg[1] + sh) > 255:
                bg[1] = 255
            else:
                bg[1] += sh
            if (bg[2] + sh) > 255:
                bg[2] = 255  
            else:
                bg[2] += sh
            print bg
            self.image.fill((bg[0], bg[1], bg[2]), ((1, 1), (self.rect.width - 2, 1)))          # Paint it to the canvas.

    def manageEvent(self, event, caller, withinBounds=True):
        # Subclass the UIView's manageEvent traverse function.
        UIView.manageEvent(self, event, caller, withinBounds)   # Allow the UIButton to still send events to lower objects by using UIView's definition. Also allows for custom callbacks
        self.manageClickDown(withinBounds, event)               # Also allow painting the up and down states for the UIButton (hence making it a button)

    def manageClickDown(self, withinBounds, event):
        # Manage the painting for up and down states
        if withinBounds:                                                                # Check if within the button. - Within
            if event.type == pygame.MOUSEBUTTONDOWN and self.state == "up":                 # See if the mouse has been pressed down ,and check the state of the button if it's already up/down to save on extra useless rendering
                self.state = "down"                                                         # Set the state for later reference/caching
                self.paint()                                                                # Re-paint the button
                self.setText()                                                              # Add the text to the button
                self.parent.updateView()                                                    # Update the parentView, which will traverse up the tree.
        if event.type == pygame.MOUSEBUTTONUP and self.state == "down":                # See if the button was pressed up, AND, it's state is already down - this needs a repaint to make it look like it's not pressed down
            self.state = "up"                                                               # Set state for later reference/caching
            self.paint()                                                                    # Re-paint the button
            self.setText(False)                                                             # add the text for the button
            self.parent.updateView()                                                        # Update the parentView, which will traverse up the tree.

        # print ("Setting state to: " + self.state)