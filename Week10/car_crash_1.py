"""
 Name: car_crash_1.py
 Author: Jessica Soler
 Date: 3/22/24
 Purpose: PyGame Hello World, an empty window
"""
# pip install pygame-ce
# import pygame library
import pygame
# import exit for a clean program shutdown
from sys import exit
# CONSTANT variables
# width and height of program window
WIDTH = 400
HEIGHT = 600
# initialize the pygame game engine
pygame.init()
# create the game surface width (x) and height (y) as tuple
surface = pygame.display.set_mode((WIDTH, HEIGHT))
# set window caption/title
pygame.display.set_caption("Car Crash")
# setup computer clock object to control the speed of the game
# this ensures the game runs at consistent speed across different systems
clock = pygame.time.Clock()
# infinate loop, aka game loop, manages the game's ongoing process
# the game loop keeps the game running smoothly
# handles input, updating the game state, rendering graphics, and repeating
# allows the games to react to user actions in real-time and maintain a coherent and engaging experience
# loop continues until game is exited or a specific condition is met
while True:
 # listen for all window events
 for event in pygame.event.get():
 
 # closing the program causes the QUIT event to be fired
 if event.type == pygame.QUIT:
 # quit pygame
 pygame.quit()
 # exit python
 exit()
 
 # from backbuffer, update pygame display to reflect any changes
 # this updates the display to show changes made in the current frame
 # essential for rendering the drawn circle on the screen
 pygame.display.update()
 
 # cap game speed to 60 frames per second
 # uses the clock object and ensures the game runs at a consistent frame rate
 # providing smooth animation
 clock.tick(60)
 
