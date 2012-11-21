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
        # print("DICKS")
        cont = constants() 
        UIView.__init__(self, dimensions, parent)
        self.userText = ""
        self.state = "up"
        self.backgroundcolor = (96, 117, 146)
        # self.backgroundcolor = (200, 117, 96)
        self.paint()
        self.font = cont.defaultButtonFont              # set the font, default is the default from constants
        self.textOffset = (0, 0)                        # set the text offset, default there is none
        
        
        
    def setBackgroundColor(self, color):
        # print "Setting BG COCKS"
        self.backgroundcolor = color
        # self.state = "up"
        self.paint()
        self.setText()
        # self.updateView()

    def setText(self, text=False):
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

    def updateView(self):
        # self.paint()
        UIView.updateView(self)

    def paint(self):
        self.image = pygame.Surface((self.rect.width, self.rect.height))                            # Fix all the rectangles.  Re-init the image
        if self.state == "down":                                                                                  # Paint accordingly whether the mouse is inside or not.
            bg = list(self.backgroundcolor)
            sh = 40                                                 # Shading scale up - Larger the number, the brighter the shaddow
            d = 2                                                   # Shading dithering value, the greater the number, the more dithered colours will be.
            sh2 = [0,0,0]
            self.image.fill((bg[0]/d + sh, bg[1]/d + sh, bg[2]/d + sh), ((1, 1), (self.rect.width - 2, self.rect.height - 2)))
        else:
            # print "WITHIN BROOOO"
            bg = list(self.backgroundcolor)
            self.image.fill(self.backgroundcolor, ((1, 1), (self.rect.width - 2, self.rect.height - 2)))
            sh = 100
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
            self.image.fill((bg[0], bg[1], bg[2]), ((1, 1), (self.rect.width - 2, 1)))

    def manageEvent(self, event, caller, withinBounds=True):
        UIView.manageEvent(self, event, caller, withinBounds)
        self.manageClickDown(withinBounds, event)

    def manageClickDown(self, withinBounds, event):
        print ("Managing clickdown")
        if withinBounds:
            print ("And we're in bounds")
            if event.type == pygame.MOUSEBUTTONDOWN and self.state == "up":
                self.state = "down"
                self.paint()
                self.setText()
                self.parent.updateView()
        if event.type == pygame.MOUSEBUTTONUP and self.state == "down":
            self.state = "up"
            self.paint()
            self.setText(False)
            self.parent.updateView()

        # print ("Setting state to: " + self.state)