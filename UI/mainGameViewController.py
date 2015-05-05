
import pygame
import NWPi
import random

class mainGameViewController(NWPi.viewController):
    def checkThreeInARow(self):
        # MEthod to check if a winner is present.
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
                                        # Found a winnner, set the winner variable with the winner name

                        # # Check on the vertical plane
                        if (i + 1) < len(self.squares):
                            if self.squares[i + 1][i2].taken and (self.squares[i + 1][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                                if (i + 2) < len(self.squares):
                                    if self.squares[i + 2][i2].taken and (self.squares[i + 2][i2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy
                                        # Found a winnner, set the winner variable with the winner name

                        # Check on the diagonal down right plane
                        if ((i + 1) < len(self.squares)) and ((i2 + 1) < len(self.squares[i])):
                            if self.squares[i + 1][i2 + 1].taken and (self.squares[i + 1][i2 + 1].occupiedBy == self.squares[i][i2].occupiedBy):
                                if ((i + 2) < len(self.squares)) and ((i2 + 2) < len(self.squares[i])):
                                    if self.squares[i + 2][i2 + 2].taken and (self.squares[i + 2][i2 + 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy
                                        # Found a winnner, set the winner variable with the winner name

                        # Check on the diagonal down left plane.
                        if ((i + 1) < len(self.squares)) and ((i2 - 1) >= 0):
                            if self.squares[i + 1][i2 - 1].taken and (self.squares[i + 1][i2 - 1].occupiedBy == self.squares[i][i2].occupiedBy):
                                if ((i + 2) < len(self.squares)) and ((i2 - 2) >= 0):
                                    if self.squares[i + 2][i2 - 2].taken and (self.squares[i + 2][i2 - 2].occupiedBy == self.squares[i][i2].occupiedBy):
                                        winner = self.squares[i][i2].occupiedBy
                                        # Found a winnner, set the winner variable with the winner name
                    drawCounter += 1
                i2 +=1
            i += 1

        if winner != False:
            # IF a winner was found, show a UIAlertView and display the winning message
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
            # Make a callback on the UIView to be run on close - will reset the gameboard.
            def action(self, event, caller, withinBounds):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.parent.parent.resetBoard()

            alert.okayAction = action

        # A Winner wasn't found, instead, it's a draw
        if drawCounter >= len(self.squares) * len(self.squares[0]) and winner == False:
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
        # Game board generation method. 
        # Pretty simple once broken down.

        # Set some intitial constants
        rows = 6            # Set how many rows the gameboard should have
        padd = 1            # Set how much padding should be between each sqaure
        cols = 6            # Set how many columns there should be
        viewWid = gameView.rect.width               # shorten the variable name to the overall viewWidth
        viewHeight = gameView.rect.height           # ~~ same with the height

        colwid = viewWid/cols                       # Determine how much width needs to be assigned to each columns depending on the width and the amount of columns
        colheight = viewHeight/rows                 # ~~ similarly with the rows

        gameView.colWd = colwid                     # allow global reference.
        gameView.rowHt = colheight                  # ~~ 


        d = 0                                       # Set an initial counter for the randomBlackSquares
        randomBlackSqaures = []                     # Set an empty list
        while d < random.randint(rows * cols / 8, rows * cols / 2):         # begin generating a random amout of black squares, depending on the size of the board.
            col = random.randint(0, cols - 1)                                   # Get a random column value
            row = random.randint(0, rows - 1)                                   # Get a random row value
            randomBlackSqaures.append((col, row))                               # add these to a tuple set for later reference and positioning of this black square
            d += 1                                                              # Increment the counter

        d2 = 0                                      # Set an initial counter for the randomSquiggleSqaures
        randomSquiggleSqaures = []                  # Set an empty list
        while d2 < random.randint(7,14):            # Create a random amount of these, between 7 and 14
            col = random.randint(0, cols - 1)           # Get a random column value
            row = random.randint(0, rows - 1)           # get a ranodom row value
            randomSquiggleSqaures.append((col, row))    # add the tuple set, along with positioning, etc
            d2 += 1                                     # incremment the counter

        # Defintiions for callbacks on the clicking of the squares when a user is to click down on a square.
        def customCallback(self, event, caller, within): 
            if event.type == pygame.MOUSEBUTTONUP:                                      # Ensure it's amouseup event
                if self.taken == False:                                                       # Make sure it's not already taken
                    if within:                                                                      # Yes, ensure the mouse is within. 
                        self.taken = True                                                               # Set the objects taken value, so it cannot be changed again
                        if self.parent.parent.turn == "PLAYER1":                                            # Check who's turn it is. Fill the square with the players counter accordingly. Pretty simple
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('cross.png')
                            self.parent.parent.turn = "PLAYER2"     
                            self.occupiedBy = "PLAYER1"                                                     # Say that it is now taken by a PLAYER1 for use in the check three in a row method
                        else:
                            subImageforsquare = NWPi.UIView((0,0), self, (0,0,0))
                            subImageforsquare.setBackgroundImage('circle.png')
                            self.parent.parent.turn = "PLAYER1"
                            self.occupiedBy = "PLAYER2"
                        subImageforsquare.rect.centerx = caller.colWd / 2                       # Position the players counter in the exact middle of the square
                        subImageforsquare.rect.centery = caller.rowHt / 2                       # ~~~

                        self.addSubView(subImageforsquare)                                      # Add the subImage/counter icon to the square for display to the user.
                        caller.updateView()                                                     # Update the gameView
                        self.parent.parent.checkThreeInARow()                                   # Check if this new addition to the game board has made a three in a row.
        
        def squiggleSqaureCallback(self, event, caller, within):
            if event.type == pygame.MOUSEBUTTONUP:                                  # Ensure it's a mouseup event
                if self.taken == False:                                                 # And that the object isn't taken,
                    if within:                                                              # If, the mouse did click within the squiggle,
                        self.taken = True                                                       # Make it marked as taken so it cannot be overwritten again
                        self.occupiedBy = "SQUIGGLE"                                                # Say that it is now taken by a squiggle for use in the check three in a row method
                        subImageforsquare = NWPi.UIView((50,50), self, (255,0,0))                   # Make a subView ready for the squiggle image
                        subImageforsquare.setBackgroundImage('squiggle.png')                        # Load the squiggle image

                        subImageforsquare.rect.centerx = caller.colWd / 2                           # Position the icon in the exact middle of the square
                        subImageforsquare.rect.centery = caller.rowHt / 2                           # ~~

                        if self.parent.parent.turn == "PLAYER1":                                    # Determine who's turn it is. Toggle the turns around, ensuring the player who clicked the square will miss their turn
                            self.parent.parent.turn = "PLAYER2"
                        elif self.parent.parent.turn == "PLAYER2":
                            self.parent.parent.turn = "PLAYER1"

                        self.addSubView(subImageforsquare)                                          # Add the subView for the new square
                        self.parent.parent.checkThreeInARow()                                       # Check if the three in a row has been made
                        caller.updateView()                                                         # Update all the views and stuff
        

        # Some counter variables for the following loop
        i = 0       # counter for the row
        i2 = 0      # counter for the columns
        self.squares = {}
        coords = [0,0]

        while i < rows:
            self.squares[i] = {}
            while i2 < cols:
                self.squares[i][i2] = NWPi.UIView((colwid, colheight), gameView, (236, 236, 236))
                self.squares[i][i2].rect.x, self.squares[i][i2].rect.y = coords
                self.squares[i][i2].setCustomCallback(customCallback)
                self.squares[i][i2].taken = False
                self.squares[i][i2].occupiedBy = "NULL"
                if (i, i2) in randomBlackSqaures:
                    subImageforsquare = NWPi.UIView((self.squares[i][i2].rect.width, self.squares[i][i2].rect.height), self, (50, 50, 50))
                    self.squares[i][i2].occupiedBy = "BLACKOUT"
                    self.squares[i][i2].taken = True
                    subImageforsquare.rect.centerx = gameView.colWd / 2
                    subImageforsquare.rect.centery = gameView.rowHt / 2
                    self.squares[i][i2].addSubView(subImageforsquare)
                elif (i, i2) in randomSquiggleSqaures:
                    self.squares[i][i2].setCustomCallback(squiggleSqaureCallback)
                    subImageforsquare = NWPi.UIView((self.squares[i][i2].rect.width, self.squares[i][i2].rect.height), self, (236, 236, 236))
                    self.squares[i][i2].addSubView(subImageforsquare)

                gameView.addSubView(self.squares[i][i2])
                self.squares[i][i2].position = [i2, i]
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


        self.whoseTurnView = NWPi.UIView((leftColView.rect.width - 1, 120), leftColView, (233,233,233), (0,0,1,0), (160,160,160))    # initialize another UIView to show who's turn it is on the left bar
        self.whoseTurnView.rect.y = 91                                      # Set coordinates
        self.updateTurnView()                                               # Update this who's turn view with the current persons turn information
        leftColView.addSubView(self.whoseTurnView)                          # Add all of these to the parent classes
        leftColView.addSubView(topButtonBorderView)                         # ~~ once again

        self.addSubView(leftColView)                                        # Add the left column to the gameControllerView

        # Initialize the gameView UIView. Set it's coordinates, etc.
        self.gameView = NWPi.UIView((self.canvas.get_rect().width - leftColView.rect.width, self.canvas.get_rect().height), self, (130, 130, 130)) 
        self.gameView.rect.x = leftColView.rect.width
        self.addSubView(self.gameView)
        self.generateGameBoard(self.gameView) # Run the gameboard generation method. woo!

    def updateTurnView(self):
        self.whoseTurnView.clearSubviews()      # Remove all objects already on the whosturnView, as we want a clean slate to draw onto

        turnIcon = NWPi.UIView((0, 0), self.whoseTurnView, (236, 236, 236))         # Create an empty UIView to load the turnview onto
        if self.turn == "PLAYER1":                                                      # Check who's turn it is, and set the background image corresponding. Easy as pi.
            turnIcon.setBackgroundImage('cross.png')
            turnIcon.rect.centerx = self.whoseTurnView.rect.width / 2
            turnIcon.rect.y = 15
           
            turnText = NWPi.textObject("Player 1 To Move")                             # Also set the text.
            turnText.rect.centerx = self.whoseTurnView.rect.width / 2
            turnText.rect.y = 85
            
        elif self.turn == "PLAYER2":
            turnIcon.setBackgroundImage('circle.png')
            turnIcon.rect.centerx = self.whoseTurnView.rect.width / 2
            turnIcon.rect.y = 15

            turnText = NWPi.textObject("Player 2 To Move")
            turnText.rect.centerx = self.whoseTurnView.rect.width / 2
            turnText.rect.y = 85

        self.whoseTurnView.addSubView(turnIcon)                                 # Add all the subViews, and win. 
        self.whoseTurnView.addSubView(turnText)
        self.whoseTurnView.updateView()                                         # Finally, update the view so everything blits, and we're good to go :D





