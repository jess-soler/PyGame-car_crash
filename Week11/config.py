"""
 Name: config.py
 Author: Jessica Soler
 Date: 3/28/24
 Purpose: global variables and constants for the entire program
"""
import pygame
import config
from sys import exit

# initialize constants for screen size
WIDTH = 400
HEIGHT = 600

class CarCrash:
    def __init__(self):
    
        # initialize the pygame library
        pygame.init()
    
        # create the game surface (window)
        self.surface = pygame.display.set_mode(
            (config.WIDTH, config.HEIGHT)
        )
        
        # set window caption
        pygame.display.set_caption("Car Crash")
        
        # load backgroundimage from file into an image variable
        self.background = pygame.image.load(
            "./assets/street.png").convert_alpha()
        
        # setup computer clock object to control the speed of the game
        self.clock = pygame.time.Clock()
        
class Color:
    def __init__(self):
        pygame.init()
        
        BLACK = pygame.Color(0, 0, 0)
        WHITE = pygame.Color (255, 255, 255)
        GREY = pygame.Color(128, 128, 128)
        RED = pygame.Color(255, 0, 0)