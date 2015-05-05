
# Basic image handling functions. These can be called globally.
# Needed for easily importing images from the data folder.
import os                       # import OS for file paths
import pygame                   # import pygame for fonts, etc
from pygame.locals import *     # get the pygame local variables


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)                       # Grab the full file path of the images directory (data/file.png)
    try:
        image = pygame.image.load(fullname)                     # catch exceptions if the file isn't found
    except pygame.error:
        # print 'Cannot load image:', fullname
        noticer("Cannot load image: " + str(fullname), 2)       # Warn the user
        # raise SystemExit, message
    image = image.convert()                                     # convert the image to a pygame surface object
    if colorkey is not None:                                    # check colour keying, allows pngs and other files to be imported
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_image_without_rect(name, colorkey=None):
    fullname = os.path.join('data', name)                       # Grab the full file path of the images directory (data/file.png)
    try:
        image = pygame.image.load(fullname)                     # catch exceptions if the file isn't found
    except pygame.error:
        noticer("Cannot load image: " + str(fullname), 2)       # warn the user
    image = image.convert()
    if colorkey is not None:                                    # convert the image to a pygame surface object
        if colorkey is -1:                                      # check colour keying, allows pngs and other files to be imported
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
