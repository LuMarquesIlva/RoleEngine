from input import Input
import pygame

class RoleEngine:
    DISPLAY = pygame.display
    BG_COLOR = (15, 15, 15, 255)
    displaySurface = None
    displayCaption = "Blank"

    def Quit():
        pygame.quit()

    class Init:
        index = 0

        def __init__(self):
            if RoleEngine.Init.index == 0:
                pygame.init()
                Input.Joystick.checkForJoysticks()
                RoleEngine.Display.setFramerateLimit(30)
                RoleEngine.Init._InitDisplay((640, 480), f"RoleEngine - {RoleEngine.displayCaption}")
                RoleEngine.Display.Fill(RoleEngine.BG_COLOR)
                RoleEngine.Init.index += 1
            else:
                pass

        def _InitDisplay(resolution = tuple, caption = str):
            Input.setRunVar(True)
            RoleEngine.DISPLAY.set_caption(caption)
            RoleEngine.displaySurface = RoleEngine.DISPLAY.set_mode(resolution)

    class Display:
        clock = pygame.time.Clock()

        def setResolution(resolution = tuple):
            RoleEngine.displaySurface = RoleEngine.DISPLAY.set_mode(resolution)

        def getResolution():
            return RoleEngine.DISPLAY.get_window_size()
        
        def setFullCaption(caption = str):
            RoleEngine.DISPLAY.set_caption(caption)
        
        def setCaption(caption = str):
            RoleEngine.displayCaption = caption
            RoleEngine.DISPLAY.set_caption(f"RoleEngine - {RoleEngine.displayCaption}")

        def getCaption():
            return RoleEngine.DISPLAY.get_caption()
        
        def Fill(color = tuple):
            RoleEngine.displaySurface.fill(color)
        
        def Update():
            RoleEngine.DISPLAY.update()

        def setFramerateLimit(value = int):
            RoleEngine.Display.clock.tick(value)