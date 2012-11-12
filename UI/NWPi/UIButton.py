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


class UIButton(pygame.sprite.Sprite):
    def __init__(self, dimensions):                     # initialise method
        cont = constants()                              # Grab the constants
        pygame.sprite.Sprite.__init__(self)             # Initialise as subclass of pyGame sprite
        self.image = pygame.Surface(dimensions)         # Draw an image using surface
        self.rect = self.image.get_rect()               # Set the rectangle of the sprite to the rect of the image we drew
        self.state = "up"                               # set the buttons current state
        self.paint()                                    # paint the colours to the button
        self.textOffset = (0, 0)                        # set the text offset, default there is none
        self.font = cont.defaultButtonFont              # set the font, default is the default from constants
        self.userText = ""
    def paint(self, within=False):
        # Painting method, used to paint colours to the UIButton
        self.image = pygame.Surface((self.rect.width, self.rect.height))                            # Fix all the rectangles.  Re-init the image
        if within:                                                                                  # Paint accordingly whether the mouse is inside or not.
            self.image.fill((68, 81, 98), ((1, 1), (self.rect.width - 2, self.rect.height - 2)))
        else:
            self.image.fill((96, 117, 146), ((1, 1), (self.rect.width - 2, self.rect.height - 2)))
            self.image.fill((239, 239, 239), ((1, 1), (self.rect.width - 2, 1)))

    def setCustomCallback(self, callback):
        # Allows setting of a callback on a button.
        self.actions = callback

    def userCallback(self, event, caller):
        # Method to run the users custom callback. This will catch fatal exceptions (luckily)
        try:
            self.actions(self, event, caller)
            # Method exists, and was used.
        except (AttributeError, TypeError):
            # Method does not exist.  What now?
            noticer("Method self.actions() does not exist", 2, self)

    def set_rect(rect):
        # Method to simply set the rectangle of this sprite
        self.rect = rect    # set the rectangle
        self.paint()        # Re-paint the image with the new dimensions
        self.setText()      # Better pop some text back onto that image

    def setText(self, text=False):
        # Method to do text rendering. Simply renders text and blits it to the surface of this object.
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

    def runCallback(self, event, caller, withinBounds=True):
        # Manager method for the callback.
        # Will handle mouse clicks as if they are mousedowns for button effects.
        # It will also send the mouseclicks to the user preset callback (if set)
        if withinBounds:
            self.userCallback(event, caller)
        # self.rect.x += 5
            if event.type == pygame.MOUSEBUTTONDOWN and self.state == "up":
                self.state = "down"
                self.paint(True)
                self.setText()
                caller.updateView()
        if event.type == pygame.MOUSEBUTTONUP and self.state == "down":
            self.state = "up"
            self.paint(False)
            self.setText(False)
            caller.updateView()
