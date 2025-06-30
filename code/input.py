import pygame

class UpdateDisplayInput():
    runVar = bool

    def __init__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                UpdateDisplayInput.setRunVar(False)
                break
    
    def setRunVar(runVar = bool):
        UpdateDisplayInput.runVar = runVar
    
    def getRunVar():
        return UpdateDisplayInput.runVar

class Input:
    class Keyboard:
        def __init__(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event:
                        case pygame.K_UP:
                            print("UP")
                        case _:
                            print("Could not get Input")