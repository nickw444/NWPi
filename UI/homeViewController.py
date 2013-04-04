#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi
import sys

class homeViewController(NWPi.viewController):
    def customInitial(self):
        self.constants = NWPi.constants()
        title = NWPi.textObject("squares", pygame.font.Font(self.constants.fancyFont, 70), True)
        title.rect.centerx = self.canvas.get_rect().centerx
        title.rect.y = 30
        self.addSubView(title, False)

        subtitle = NWPi.textObject("By Nick and Dylan", pygame.font.Font(self.constants.fancyFont, 25), True)
        subtitle.rect.centerx = self.canvas.get_rect().centerx
        subtitle.rect.y = 100
        self.addSubView(subtitle, False)

        def showViewOne(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("GAMEVIEW")

        button = NWPi.fancyButton(self)
        # Initialise a button, easy as pi
        button.setText("Play Game")
        # Put some text on that button
        button.rect.centerx = self.canvas.get_rect().centerx
        # Set the center position of the button
        button.rect.y = 200
        # Offset it from the top a bit
        button.setCustomCallback(showViewOne)
        # Add the callback to the object
        self.addSubView(button, True)
        # Add the object to the current View.

        def showViewTwo(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("INSTRUCTIONS")

        button2 = NWPi.fancyButton(self)
        # Initialise a button, easy as pi
        button2.setText("Instructions")
        # Put some text on that button
        button2.rect.centerx = self.canvas.get_rect().centerx
        # Set the center position of the button
        button2.rect.y = 300
        # Offset it from the top a bit
        button2.setCustomCallback(showViewTwo)
        # button2.setBackgroundColor((160,128,128))
        # Add the callback to the object
        self.addSubView(button2, True)
        # Add the object to the current View.

        def quit(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                sys.exit()


        quitButton = NWPi.UIButton((60, 30), self)
        # Initialise a button, easy as pi
        quitButton.setText("Quit")
        # Put some text on that button
        quitButton.rect.x = 30
        # Set the center position of the button
        quitButton.rect.y = 550
        # Offset it from the top a bit
        quitButton.setCustomCallback(quit)
        quitButton.setBackgroundColor((170,110, 110))
        # button2.setBackgroundColor((160,128,128))
        # Add the callback to the object
        self.addSubView(quitButton, True)
        # Add the object to the current View.



