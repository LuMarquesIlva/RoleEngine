import pygame

class Display:
        DISPLAY = pygame.display
        BG_COLOR = (15, 15, 15, 255)
        displaySurface = None
        displayCaption = "Blank"

        clock = pygame.time.Clock()

        def setResolution(resolution = tuple):
            Display.displaySurface = Display.DISPLAY.set_mode(resolution)

        def getResolution():
            return Display.DISPLAY.get_window_size()
        
        def setFullCaption(caption = str):
            Display.DISPLAY.set_caption(caption)
        
        def setCaption(caption = str):
            Display.displayCaption = caption
            Display.DISPLAY.set_caption(f"RoleEngine - {Display.displayCaption}")

        def getCaption():
            return Display.DISPLAY.get_caption()
        
        def Fill(color = tuple):
            Display.displaySurface.fill(color)
        
        def Update():
            Display.DISPLAY.update()

        def setFramerateLimit(value = int):
            Display.clock.tick(value)
        
        #TODO fix this
        def setWindowIcon(icon = __file__):
            icon = pygame.surface.Surface((124, 124))
            window = pygame.window.Window.id
            pygame.Window.set_icon(window, icon)