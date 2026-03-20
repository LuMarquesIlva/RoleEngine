from scripts.display import Display
from scripts.input import Input

import pygame


class RoleEngine:
    
    class Init:
        index = 0

        def __init__(self):
            super()
            if RoleEngine.Init.index == 0:
                pygame.joystick.init()
                Input.Joystick.checkForJoysticks()
                RoleEngine.Init._InitDisplay((640, 480), f"RoleEngine - {Display.displayCaption}")
                Display.setFramerateLimit(30)
                Display.Fill(Display.BG_COLOR)
                # RoleEngine.Display.setWindowIcon("../images/RoleEngineIconPH.png")"""
                RoleEngine.Init.index += 1

        def _InitDisplay(resolution=tuple, caption=str):
            Input.setRunVar(True)
            Display.DISPLAY.set_caption(caption)
            Display.setResolution(resolution)
