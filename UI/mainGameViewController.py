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
        self.addSubView(button2, True)


        view = NWPi.UIView((300,30), self, (0,255,0))
        view.rect.x = 10
        view.rect.y = 70
        self.addSubView(view)

        subb = NWPi.UIView((30, 30), view, (255,0,0))
        subb.rect.x = 5
        subb.rect.y = 5
        view.addSubView(subb)

        subb.updateView()
        