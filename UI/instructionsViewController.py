#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi


class instructionsViewController(NWPi.viewController):
    def customInitial(self):
        text = NWPi.textObject("Layout Two", False, True)
        text.rect.centerx = self.canvas.get_rect().centerx
        text.rect.y = 200
        self.addSubView(text)

        def backToHome(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")

        homeButton = NWPi.UIButton((170, 40), self)
        homeButton.setText("Awesome, I Understand")
        homeButton.rect.centerx = self.canvas.get_rect().centerx
        homeButton.rect.y = 450
        homeButton.setCustomCallback(backToHome)
        
        instructions = NWPi.UIView((0,0), self)
        instructions.setBackgroundImage("instructions.png")
        instructions.rect.centerx = self.get_rect().width / 2

        self.addSubView(instructions)

        self.addSubView(homeButton, True)

        self.setBackgroundColor((236,236,236))
