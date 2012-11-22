#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################


import pygame               # Import pygame
import UI                   # Import all the View Controllers we have custom defined
import UI.NWPi as NWPi      # Import the NWPi Framework for local reference. (Nick's Awesome Framework)
import sys                  # Import the system library. We use this to quit the mainprogram

# Split up the events loop away from the main initialisation for easier reading.
def loop():
    for event in pygame.event.get():            # Loop through each event in the pygame events buffer
        # print("COCKS")
        if event.type == pygame.QUIT:           # Check if the event happens to be a quitting event.
            sys.exit()                         # If it is, QUIT pygame.
        elif (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN):  # or event.type == pygame.MOUSEMOTION
            # Check if the event is a mousebuttonup/down. We /could/ check for mousemove, but we don't need it, nothing is hovering. Waste of resources
            if (event.button != 5 and event.button != 4):   # Make sure the button isn't the scrollwheel. Shit gets awkward if it was.
                for object in topLevelObjects:              # Loop through all RootViews (Should only be one, but it's expandable, hence using a list)
                    object.manageEvent(event)               # On the object for the topLevel Loop, we send the event down to it, the ViewController will now manage the event from here
        # elif (event.type == pygame.MOUSEMOTION):
        #         for object in topLevelObjects:              # Loop through all RootViews (Should only be one, but it's expandable, hence using a list)
        #             object.manageEvent(event)
        pygame.display.flip()

# ! Main Game
def main():
    # The topLevelObjects is a list to store objects at the top level to listen for events.
    # A typical use should only have the navigationViewController inside it as the subclasses manage events
    global topLevelObjects      # Allow for the topLevelObjects list to be used elsewhere
    topLevelObjects = []

    # Initialise screen and pyGame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # Set the window title
    pygame.display.set_caption('Squares')

    # initialisation of the navigation controller.
    navigationViewController = NWPi.navigationController(screen)             # Create a navigation view controller. Will parent all the Viewcontrollers
    topLevelObjects.append(navigationViewController)                    # This will now be added to topLevelObjects so it can recieve events

    # draw each viewController to the navigation controller
    home = UI.homeViewController(navigationViewController)                 # Create a ViewController, from subclass homeViewController where all elements are already defined
    navigationViewController.addSubView("HOMEVIEWCONTROLLER", home)     # Add the ViewController to the navigation Controller. Do the same with the rest.

    secondView = UI.instructionsViewController(navigationViewController)
    navigationViewController.addSubView("INSTRUCTIONS", secondView)

    gameView = UI.mainGameViewController(navigationViewController)
    navigationViewController.addSubView("GAMEVIEW", gameView)

    # We need to set a viewController to show as the top level. Choose it here:
    navigationViewController.makeKeyAndVisible("INSTRUCTIONS")    # Tell the navigation controller to set the view with the specified identifier to the top

    # We need a loop to keep the script running. Defining it here
    while True:
        loop()  # Run the loop() function we defined earlier.
if __name__ == '__main__':      # Allow for use as a module in an upper class. Run the main loop if this IS the main program
    main()                      # Run the main loop
