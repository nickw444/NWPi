#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi


class firstAlternativeView(NWPi.viewController):
    def customInitial(self):
        self.constants = NWPi.constants()
        text = NWPi.textObject("Layout One", False, True)
        text.rect.centerx = self.canvas.get_rect().centerx
        text.rect.y = 200
        self.addSubView(text)

        def backToHome(self, event, caller):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")

        homeButton = NWPi.fancyButton()
        homeButton.setText("Go Home!")
        homeButton.rect.centerx = self.canvas.get_rect().centerx
        homeButton.rect.y = 450
        homeButton.setCustomCallback(backToHome)
        self.addSubView(homeButton, True)
