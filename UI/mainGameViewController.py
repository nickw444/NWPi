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
        self.updateTurnView()
        winner = False
        drawCounter = 0
        i = 0
        while i <  len(self.squares):
            i2 = 0
            while i2 < len(self.squares[i]):
                if self.squares[i][i2].taken:
                    if (self.squares[i][i2].occupiedBy == "PLAYER1" or self.squares[i][i2].occupiedBy == "PLAYER2"):
                        # Check on the horizontal plane
                        if (i2 + 1) < len(self.squares[i]):
                            if self.squares[i][i2 + 1].taken and (self.squares[i][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy):
                                if (i2 + 2) < len(self.squares[i]):
                                    if self.squares[i][i2 + 2].taken and (self.squares[i][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy

                        # # Check on the vertical plane
                        if (i + 1) < len(self.squares):
                            if self.squares[i + 1][i2].taken and (self.squares[i + 1][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                                if (i + 2) < len(self.squares):
                                    if self.squares[i + 2][i2].taken and (self.squares[i + 2][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy
                        # Check on the diagonal down right plane
                        if ((i + 1) < len(self.squares)) and ((i2 + 1) < len(self.squares[i])):
                            if self.squares[i + 1][i2 + 1].taken and (self.squares[i + 1][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy):
                                if ((i + 2) < len(self.squares)) and ((i2 + 2) < len(self.squares[i])):
                                    if self.squares[i + 2][i2 + 2].taken and (self.squares[i + 2][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy

                        # Check on the diagonal down left plane.
                        if ((i + 1) < len(self.squares)) and ((i2 - 1) >= 0):
                            if self.squares[i + 1][i2 - 1].taken and (self.squares[i + 1][i2 - 1].occupiedBy == self.squares[i][i2].occupiedBy):
                                if ((i + 2) < len(self.squares)) and ((i2 - 2) >= 0):
                                    if self.squares[i + 2][i2 - 2].taken and (self.squares[i + 2][i2 - 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy
                    drawCounter += 1
                i2 +=1
            i += 1

        if winner != False:
            bg = NWPi.UIView((self.get_rect().width, self.get_rect().height), self, (0,0,0))
            bg.setOpacity(128)
            alert = NWPi.UIAlertView((300, 90), self, (240,240,240), (2,2,2,2))
            alert.bgDelegate = bg
            alert.rect.centerx = self.get_rect().width/2
            alert.rect.centery = self.get_rect().height/ 2 - 50

            if winner == "PLAYER1":
                alert.setText("Player 1 (Cross) Wins!")
            elif winner == "PLAYER2":
                alert.setText("Player 2 (Circle) Wins!")

            self.addSubView(bg)
            self.addSubView(alert)
            def action(self, event, caller, withinBounds):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.parent.parent.resetBoard()

            alert.okayAction = action

        if drawCounter >= len(self.squares) * len(self.squares[0]):
            bg = NWPi.UIView((self.get_rect().width, self.get_rect().height), self, (0,0,0))
            bg.setOpacity(128)
            alert = NWPi.UIAlertView((300, 90), self, (240,240,240), (2,2,2,2))
            alert.bgDelegate = bg
            alert.rect.centerx = self.get_rect().width/2
            alert.rect.centery = self.get_rect().height/ 2 - 50
            alert.setText("It's a Draw! No one wins :(")
            self.addSubView(bg)
            self.addSubView(alert)
            def action(self, event, caller, withinBounds):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.parent.parent.resetBoard()

            alert.okayAction = action

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
                        subImageforsquare = NWPi.UIView((50,50), self, (255,0,0))
                        subImageforsquare.setBackgroundImage('squiggle.png')

                        subImageforsquare.rect.centerx = caller.colWd / 2
                        subImageforsquare.rect.centery = caller.rowHt / 2

                        if self.parent.parent.turn == "PLAYER1":
                            self.parent.parent.turn = "PLAYER2"
                        elif self.parent.parent.turn == "PLAYER2":
                            self.parent.parent.turn = "PLAYER1"

                        self.addSubView(subImageforsquare)
                        self.parent.parent.checkThreeInARow()
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
                    self.squares[i][i2].occupiedBy = "BLACKOUT"
                    self.squares[i][i2].taken = True
                    subImageforsquare.rect.centerx = gameView.colWd / 2
                    subImageforsquare.rect.centery = gameView.rowHt / 2
                    self.squares[i][i2].addSubView(subImageforsquare)
                elif (i, i2) in randomGaySquares:
                    self.squares[i][i2].setCustomCallback(gaySqaureCallback)
                    subImageforsquare = NWPi.UIView((self.squares[i][i2].rect.width, self.squares[i][i2].rect.height), self, (236, 236, 236))
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
        self.updateView()


    def resetBoard(self):
        self.turn = "PLAYER1"
        self.gameView.clearSubviews()
        self.generateGameBoard(self.gameView)
        self.updateTurnView()

    def customInitial(self):                                        # Custom initialization method for this UIViewController
        self.turn = "PLAYER1"                                       # Set the turn for the player. Ensure player1 moves first. This variable keeps track of who's turn it is.
        self.setBackgroundColor((150,150,150))                      # Set the background color of this view. (Simple i guess?)
        

        # Define some button callbacks (explicitly the buttons to reset the board and to gohome/end game)
        def goHome(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                caller.parent.parent.resetBoard()                                                   # Reset the board, in case someone wants to come back and play later.
                caller.parent.parent.navigationController.makeKeyAndVisible("HOMEVIEWCONTROLLER")   # Navigate back to the homeViewcontroller
        
        def resetBoard(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:
                self.parent.parent.parent.turn = "PLAYER1"       # Make it player 1's turn again
                caller.parent.parent.resetBoard()                # Reset the board, regenerate

        leftColView = NWPi.UIView((220, self.canvas.get_rect().height), self, (233,233,233), (0,1,0,0))                                     # Initialize a view for the left column. Allows object nesting
        topButtonBorderView = NWPi.UIView((leftColView.rect.width - 1, 90), leftColView, (220,220,220), (0,0,1,0), (160,160,160))           # Initialize a view to place some buttons in. Give it a border below it too.

        # Lets draw some buttons. 
        # Create the backbutton
        backButton = NWPi.UIButton((180,30), topButtonBorderView)           # init a button, with parent "TopBorderView"
        backButton.rect.centerx = topButtonBorderView.rect.width /2         # Set its x position
        backButton.rect.y = 10                                              # Set its y position
        backButton.setText("End Game")                                      # Give it some text
        backButton.actions = goHome                                         # Assign the callback to the one we defined earlier
        topButtonBorderView.addSubView(backButton)                          # Add it to the topButtonBorderView UIView we created just before.

        # Create the reset button
        resetButton = NWPi.UIButton((180,30), topButtonBorderView)          # init a button, with parent "TopBorderView"
        resetButton.rect.centerx = topButtonBorderView.rect.width / 2       # Set its x position
        resetButton.rect.y = 50                                             # Set it's y position
        resetButton.setBackgroundColor((170,110, 110))                      # Give it a custom color.
        resetButton.setText("Reset Game")                                   # Set the text of the button
        resetButton.actions = resetBoard                                    # Set the callback method to the one we defined earlier
        topButtonBorderView.addSubView(resetButton)                         # Add it to the topButtonBorderView UIView we created just before.


        self.whoseTurnView = NWPi.UIView((leftColView.rect.width - 1, 120), leftColView, (233,233,233), (0,0,1,0), (160,160,160))
        self.whoseTurnView.rect.y = 91
        self.updateTurnView()
        leftColView.addSubView(self.whoseTurnView)
        leftColView.addSubView(topButtonBorderView)

        self.addSubView(leftColView)
        self.gameView = NWPi.UIView((self.canvas.get_rect().width - leftColView.rect.width, self.canvas.get_rect().height), self, (130, 130, 130))
        self.gameView.rect.x = leftColView.rect.width
        self.addSubView(self.gameView)
        self.generateGameBoard(self.gameView)

    def updateTurnView(self):
        self.whoseTurnView.clearSubviews()

        turnIcon = NWPi.UIView((0, 0), self.whoseTurnView, (236, 236, 236))
        if self.turn == "PLAYER1":
            turnIcon.setBackgroundImage('cross.png')
            turnIcon.rect.centerx = self.whoseTurnView.rect.width / 2
            turnIcon.rect.y = 15
           
            turnText = NWPi.textObject("Player 1 To Move")
            turnText.rect.centerx = self.whoseTurnView.rect.width / 2
            turnText.rect.y = 85
            
        elif self.turn == "PLAYER2":
            turnIcon.setBackgroundImage('circle.png')
            turnIcon.rect.centerx = self.whoseTurnView.rect.width / 2
            turnIcon.rect.y = 15

            turnText = NWPi.textObject("Player 2 To Move")
            turnText.rect.centerx = self.whoseTurnView.rect.width / 2
            turnText.rect.y = 85

        self.whoseTurnView.addSubView(turnIcon)
        self.whoseTurnView.addSubView(turnText)
        self.whoseTurnView.updateView()





