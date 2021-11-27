import pygame
from render import Render
from board import Board
import ctypes  # to avoid windows scaling nonsense (not required for linux or mac i guess)


SCREEN_WIDTH  = 960 #its a chess board 

''' 
basically this to avoid windows display scaling nonsense
Comment this out if you want to run this on linux
'''
ctypes.windll.user32.SetProcessDPIAware() # This basically tells windows "DO NOT SCALE THIS!!!!"


FRAMERATE = 20 # 10 will also work
 

def Game():
    b = Board()
    renderer = Render(b,SCREEN_WIDTH,FRAMERATE)

    while True:
        if renderer.update() == 'quit':
            print('Exiting')
            break
        assert 1 == 1


if __name__ == '__main__':
    Game()
