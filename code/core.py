import pygame

class RoleEngine:
    DISPLAY = pygame.display
    BG_COLOR = (15, 15, 15, 255)
    displaySurface = None
    displayCaption = "Blank"

    def Quit():
        pygame.quit()

    class Init:
        def __init__(self):
            pygame.init()
            RoleEngine.Init._InitDisplay((640, 480), f"RoleEngine - {RoleEngine.displayCaption}")
            RoleEngine.Display.Fill(RoleEngine.BG_COLOR)

        def _InitDisplay(resolution = tuple, caption = str):
            RoleEngine.DISPLAY.set_caption(caption)
            RoleEngine.displaySurface = RoleEngine.DISPLAY.set_mode(resolution)

    class Display:
        def setResolution(resolution = tuple):
            RoleEngine.displaySurface = RoleEngine.DISPLAY.set_mode(resolution)

        def getResolution():
            return RoleEngine.DISPLAY.get_window_size()
        
        def setCaption(caption = str):
            RoleEngine.DISPLAY.set_caption(caption)

        def getCaption():
            return RoleEngine.DISPLAY.get_caption()
        
        def Fill(color = tuple):
            RoleEngine.displaySurface.fill(color)
        
        def Update():
            RoleEngine.DISPLAY.update()