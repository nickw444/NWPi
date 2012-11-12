#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi


class homeViewController(NWPi.viewController):
    def customInitial(self):
        self.constants = NWPi.constants()
        title = NWPi.textObject("squares", pygame.font.Font(self.constants.fancyFont, 70), True)
        title.rect.centerx = self.canvas.get_rect().centerx
        title.rect.y = 30
        self.addSubView(title, False)

        subtitle = NWPi.textObject("By Dylan and Nick", pygame.font.Font(self.constants.fancyFont, 25), True)
        subtitle.rect.centerx = self.canvas.get_rect().centerx
        subtitle.rect.y = 100
        self.addSubView(subtitle, False)

        def showViewOne(self, event, caller):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("GAMEVIEW")

        button = NWPi.fancyButton()
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

        def showViewTwo(self, event, caller):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("THIRDVIEW")

        button2 = NWPi.fancyButton()
        # Initialise a button, easy as pi
        button2.setText("Instructions")
        # Put some text on that button
        button2.rect.centerx = self.canvas.get_rect().centerx
        # Set the center position of the button
        button2.rect.y = 300
        # Offset it from the top a bit
        button2.setCustomCallback(showViewTwo)
        # Add the callback to the object
        self.addSubView(button2, True)
        # Add the object to the current View.

        # button3 = NWPi.UIButton((160, 40))
        # button3.rect.centerx = self.canvas.get_rect().centerx
        # button3.rect.y = 500
        # button3.font = pygame.font.SysFont("Arial", 16, False, False)
        # button3.setText("Text text text")
        # self.addSubView(button3, True)

        # def moveButton(self, event, caller):
        #     self.rect.x += 1
        #     caller.updateView()     
        #         # print "DICKSSSSSSSS"
        #         # print event
        #             # print 'cocks'
        #             # self.rect.x = event.pos[0]

        # button3.setCustomCallback(moveButton)
