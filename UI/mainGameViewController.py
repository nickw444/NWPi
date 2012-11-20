#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

import pygame
import NWPi
import random

class mainGameViewController(NWPi.viewController):
    def checkThreeInARow(self):
        i = 0
        while i <  len(self.squares):
            i2 = 0
            while i2 < len(self.squares[i]):
                # print self.squares[i][i2].taken
                if self.squares[i][i2].taken and (self.squares[i][i2].occupiedBy == "PLAYER1" or self.squares[i][i2].occupiedBy == "PLAYER2"):
                    # print self.squares[i][i2].occupiedBy
                    if (i2 + 1) < len(self.squares[i]):
                        if self.squares[i][i2 + 1].taken and (self.squares[i][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy):
                            print("Found second " + self.squares[i][i2 + 1].occupiedBy)
                            if (i2 + 2) < len(self.squares[i]):
                                if self.squares[i][i2 + 2].taken and (self.squares[i][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                    print("Found third " + self.squares[i][i2 + 2].occupiedBy)
                                    print("Three in a row found horizontally")

                    # # Check on the vertical plane
                    if (i + 1) < len(self.squares):
                        if self.squares[i + 1][i2].taken and (self.squares[i + 1][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                            if (i + 2) < len(self.squares):
                                if self.squares[i + 2][i2].taken and (self.squares[i + 2][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                                    print("Three in a row vertically")

                    if ((i + 1) < len(self.squares)) and ((i2 + 1) < len(self.squares[i])):
                        if self.squares[i + 1][i2 + 1].taken and (self.squares[i + 1][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy):
                            if ((i + 2) < len(self.squares)) and ((i2 + 2) < len(self.squares[i])):
                                if self.squares[i + 2][i2 + 2].taken and (self.squares[i + 2][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                    print("Three in a row diagonally down right")


                    if ((i + 1) < len(self.squares)) and ((i2 - 1) >= 0):
                        if self.squares[i + 1][i2 - 1].taken and (self.squares[i + 1][i2 - 1].occupiedBy == self.squares[i][i2].occupiedBy):
                            if ((i + 2) < len(self.squares)) and ((i2 - 2) >= 0):
                                if self.squares[i + 2][i2 - 2].taken and (self.squares[i + 2][i2 - 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                    print("Three in a row diagonally down left")

                    # if self.squares[i][i2 + 1].taken and self.squares[i][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy:
                    #     # the one to the right is also taken
                    #     if self.squares[i][i2 + 2].taken and self.squares[i][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy:
                    #         # there are three in a row.
                    #         print ("WE HAVE A WINNER")
                i2 +=1
            i += 1

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
        self.squares = {}
        coords = [0,0]

        # randomTriSquares = [(0,2), (2,2)]

        d = 0
        randomTriSquares = []
        while d < random.randint(rows * cols / 8, rows * cols / 2):
            col = random.randint(0, cols - 1)
            row = random.randint(0, rows - 1)
            randomTriSquares.append((col, row))
            d += 1

        d2 = 0
        randomGaySquares = []
        while d2 < random.randint(7,14):
            col = random.randint(0, cols - 1)
            row = random.randint(0, rows - 1)
            randomGaySquares.append((col, row))
            d2 += 1
        print "DICKS " + str(randomGaySquares)
        def customCallback(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                if self.taken == False:
                    if within:
                        self.taken = True
                        if self.parent.parent.turn == "PLAYER1":
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('cross.png')
                            self.parent.parent.turn = "PLAYER2"
                            self.occupiedBy = "PLAYER1"
                        else:
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('circle.png')
                            self.parent.parent.turn = "PLAYER1"
                            self.occupiedBy = "PLAYER2"
                        subImageforsquare.rect.centerx = caller.colWd / 2
                        subImageforsquare.rect.centery = caller.rowHt / 2

                        self.addSubView(subImageforsquare)
                        caller.updateView()
                        print("Clicked in square: " + str(self.position[0]) + ", " + str(self.position[1]))
                        self.parent.parent.checkThreeInARow()
        def gaySqaureCallback(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                if self.taken == False:
                    if within:
                        self.taken = True
                        self.occupiedBy = "GAYSQAURE"
                        print("LOL YOU CLICKED A GAY SQUARE")
                        subImageforsquare = NWPi.UIView((50,50), self, (255,0,0))
                        subImageforsquare.setBackgroundImage('squiggle.png')

                        subImageforsquare.rect.centerx = caller.colWd / 2
                        subImageforsquare.rect.centery = caller.rowHt / 2

                        if self.parent.parent.turn == "PLAYER1":
                            self.parent.parent.turn = "PLAYER2"
                        elif self.parent.parent.turn == "PLAYER2":
                            self.parent.parent.turn = "PLAYER1"

                        self.addSubView(subImageforsquare)
                        caller.updateView()
        while i < rows:
            self.squares[i] = {}
            while i2 < cols:
                self.squares[i][i2] = NWPi.UIView((colwid, colheight), gameView, (236, 236, 236))
                self.squares[i][i2].rect.x, self.squares[i][i2].rect.y = coords
                self.squares[i][i2].setCustomCallback(customCallback)
                self.squares[i][i2].taken = False
                self.squares[i][i2].occupiedBy = "NULL"
                if (i, i2) in randomTriSquares:
                    subImageforsquare = NWPi.UIView((self.squares[i][i2].rect.width, self.squares[i][i2].rect.height), self, (50, 50, 50))
                    # subImageforsquare.setBackgroundImage('triangle.png')
                    # self.parent.parent.turn = "PLAYER1"
                    self.squares[i][i2].occupiedBy = "BLACKOUT"
                    self.squares[i][i2].taken = True
                    subImageforsquare.rect.centerx = gameView.colWd / 2
                    subImageforsquare.rect.centery = gameView.rowHt / 2
                    self.squares[i][i2].addSubView(subImageforsquare)
                elif (i, i2) in randomGaySquares:
                    print("FOUND SOME GAME SQAURES")
                    self.squares[i][i2].setCustomCallback(gaySqaureCallback)
                    subImageforsquare = NWPi.UIView((self.squares[i][i2].rect.width, self.squares[i][i2].rect.height), self, (236, 236, 236))
                    # subImageforsquare.rect.centerx = gameView.colWd / 2
                    # subImageforsquare.rect.centery = gameView.rowHt / 2
                    self.squares[i][i2].addSubView(subImageforsquare)

                gameView.addSubView(self.squares[i][i2])
                self.squares[i][i2].position = [i2, i]
                c += 1
                i2 += 1
                coords[0] += colwid + padd
            i += 1
            i2 = 0
            coords[0] = 0
            coords[1] += colheight + padd
        # self.squares[2][1].setBackgroundImage('triangle.png')
        # gameView.updateView()
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





