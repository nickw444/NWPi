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
    def generateGameBoard(self, gameView):
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
                    if within:
                        self.taken = True
                        if self.parent.parent.turn == "PLAYER1":
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('cross.png')
                            self.parent.parent.turn = "PLAYER2"
                        else:
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('circle.png')
                            self.parent.parent.turn = "PLAYER1"
                        subImageforsquare.rect.centerx = caller.colWd / 2
                        subImageforsquare.rect.centery = caller.rowHt / 2

                        self.addSubView(subImageforsquare)
                        caller.updateView()
                        print("Clicked in square: " + str(self.position[0]) + ", " + str(self.position[1]))
        while i < rows:
            squares[i] = {}
            while i2 < cols:
                squares[i][i2] = NWPi.UIView((colwid, colheight), gameView, (236, 236, 236))
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
        # print squares



    def resetBoard(self):
        self.gameView.clearSubviews()
        self.generateGameBoard(self.gameView)

    def customInitial(self):
        self.turn = "PLAYER1"
        self.setBackgroundColor((150,150,150))
        
        def goHome(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.parent.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")
        
        def resetBoard(self, event, caller, within):
            print 'woo'
            if event.type == pygame.MOUSEBUTTONUP:
                caller.parent.resetBoard()


        leftColView = NWPi.UIView((220, self.canvas.get_rect().height), self, (233,233,233), (0,1,0,0))

        backButton = NWPi.UIButton((70,30), leftColView)
        backButton.rect.x = 10
        backButton.rect.y = 10
        backButton.setText("Home")
        backButton.actions = goHome
        leftColView.addSubView(backButton)

        resetButton = NWPi.UIButton((70,30), leftColView)
        resetButton.rect.x = 90
        resetButton.rect.y = 10
        resetButton.setText("Reset")
        resetButton.actions = resetBoard
        leftColView.addSubView(resetButton)


        self.addSubView(leftColView)
        self.gameView = NWPi.UIView((self.canvas.get_rect().width - leftColView.rect.width, self.canvas.get_rect().height), self, (130, 130, 130))
        self.gameView.rect.x = leftColView.rect.width
        self.addSubView(self.gameView)
        self.generateGameBoard(self.gameView)





