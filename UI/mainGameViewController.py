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
        global turn
        turn = "PLAYER1"
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
        backButton = NWPi.UIButton((70,30), leftColView)
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

        gameView.colWd = colwid
        gameView.rowHt = colheight
        i = 0
        c = 1
        i2 = 0
        squares = {}
        coords = [0,0]
        def customCallback(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                if self.taken == False:
                    global turn
                    if within:
                        self.taken = True
                        if turn == "PLAYER1":
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('cross.png')
                            turn = "PLAYER2"
                        else:
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('circle.png')
                            turn = "PLAYER1"
                        subImageforsquare.rect.centerx = caller.colWd / 2
                        subImageforsquare.rect.centery = caller.rowHt / 2
                        # print self.rect
                        
                        self.addSubView(subImageforsquare)
                        caller.updateView()
                        print("Clicked in square: " + str(self.position[0]) + ", " + str(self.position[1]))
            # print("DICKS")
        while i < rows:
            squares[i] = {}
            while i2 < cols:
                squares[i][i2] = NWPi.UIView((colwid, colheight), self, (236, 236, 236))
                squares[i][i2].rect.x, squares[i][i2].rect.y = coords
                squares[i][i2].setCustomCallback(customCallback)
                squares[i][i2].taken = False
                gameView.addSubView(squares[i][i2])
                squares[i][i2].position = [i2, i]
                c += 1
                i2 += 1
                coords[0] += colwid + padd
            i += 1
            i2 = 0
            coords[0] = 0
            coords[1] += colheight + padd
        self.updateView()
        print squares




