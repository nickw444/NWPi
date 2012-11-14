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
        self.setBackgroundColor((150,150,150))
        # def showViewOne(self, event, caller):
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         caller.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")

        # button2 = NWPi.UIButton((70,40))
        # button2.rect.x = 10
        # button2.rect.y = 10
        # button2.setText("Home")
        # button2.setCustomCallback(showViewOne)
        # # button2.setCustomCallback(goHome)

        # # button2.actions = goHome

        # view = NWPi.UIView((220,self.canvas.get_rect().height), self, (210,210,210))
        # self.addSubView(view)

        
        # subb = NWPi.UIView((30, 30), view, (255,0,0))
        # subb.rect.x = 5
        # subb.rect.y = 50
        def goHome(self, event, caller, within):
            caller.parent.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")
        leftColView = NWPi.UIView((220, self.canvas.get_rect().height), self, (233,233,233), (0,1,0,0))
        gameView = NWPi.UIView((self.canvas.get_rect().width - leftColView.rect.width, self.canvas.get_rect().height), self, (130, 130, 130))
        gameView.rect.x = leftColView.rect.width

        # backButton = NWPi.UIView((60,60), self, (255,0,0), (5,5,5,5))
        # backButton.rect.x = 50
        # backButton.rect.y = 50
        backButton = NWPi.UIButton((70,40), leftColView)
        backButton.rect.x = 10
        backButton.rect.y = 10
        backButton.setText("Home")
        backButton.actions = goHome
        leftColView.addSubView(backButton)


        self.addSubView(leftColView)
        self.addSubView(gameView)
        rows = 6
        padd = 1
        cols = 6
        viewWid = gameView.rect.width
        viewHeight = gameView.rect.height

        colwid = viewWid/cols
        colheight = viewHeight/rows

        i = 0
        c = 1
        i2 = 0
        squares = {}
        coords = [0,0]
        def customCallback(self, event, caller, within):
            if within:
                # print self.rect
                print("Clicked in square: " + str(self.position[0]) + ", " + str(self.position[1]))
            # print("DICKS")
        while i < rows:
            while i2 < cols:
                squares[c] = NWPi.UIView((colwid, colheight), self, (236, 236, 236))
                squares[c].rect.x, squares[c].rect.y = coords
                squares[c].setCustomCallback(customCallback)
                gameView.addSubView(squares[c])
                squares[c].position = [i2, i]
                c += 1
                i2 += 1
                coords[0] += colwid + padd
            i += 1
            i2 = 0
            coords[0] = 0
            coords[1] += colheight + padd
        self.updateView()
        print squares

