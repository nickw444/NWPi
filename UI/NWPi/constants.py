#####################################################################
### Copyright Nick Whyte 2012
### All Rights Reserved (c)
### Distribution, Modification and Attribution Strictly Prohibited
### Legal Action may be taken
### http://www.nickwhyte.com/
#####################################################################

# Global constants class. Will hold ALL changable data for the game
# This file should be populated with game settings for reference later in ANY superclass.
# The rest of the class is pretty self explanatory IMO.
import os 		 # Import OS functions for File Paths
import pygame	 # Import pygame for Fonts, etc


class constants():
    def __init__(self):
        self.fancyFont = os.path.join('data', "Savoye.ttf")
        self.fancyButtonFont = pygame.font.Font(os.path.join('data', "Savoye.ttf"), 32)
        self.defaultFontSize = 16
        self.defaultFont = pygame.font.SysFont("Arial", self.defaultFontSize, False, False)
        self.defaultButtonFont = pygame.font.SysFont("Arial", 14, False, False)
