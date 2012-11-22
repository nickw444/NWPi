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
        def backToHome(self, event, caller, withinBounds):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")

        # Make a button to return home and assign the callback
        homeButton = NWPi.UIButton((170, 40), self)
        homeButton.setText("Awesome, I Understand")
        homeButton.rect.centerx = self.canvas.get_rect().centerx
        homeButton.rect.y = 450
        homeButton.setCustomCallback(backToHome)
        
        # Load the instructions in to a UIView from the instructions.png file.
        instructions = NWPi.UIView((0,0), self)
        instructions.setBackgroundImage("instructions.png")
        instructions.rect.centerx = self.get_rect().width / 2

        
        # Add all the views 
        self.addSubView(instructions)
        self.addSubView(homeButton, True)

        # Set BG color of the view
        self.setBackgroundColor((236,236,236))
