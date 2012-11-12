#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi

class mainGameViewController(NWPi.viewController):
    def customInitial(self):
        def goHome(self, event, caller):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")

        button2 = NWPi.UIButton((70,40))
        button2.rect.x = 10
        button2.rect.y = 10
        button2.setText("Home")
        button2.setCustomCallback(goHome)

        def dicks(self, event, caller):
            print("CALLBABBABABABABAB")

        view = NWPi.UIView((220,self.canvas.get_rect().height), self, (210,210,210))
        self.addSubView(view)

        view.addSubView(button2)
        subb = NWPi.UIView((30, 30), view, (255,0,0))
        subb.rect.x = 5
        subb.rect.y = 50
        view.setCustomCallback(dicks)
        subb.addBorders((1,1,1,1))
        view.addSubView(subb)


        # subb.updateView()

