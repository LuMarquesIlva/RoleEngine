import pygame

class DisplayInput():
    runVar = bool

    def Update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DisplayInput.setRunVar(False)
                break
    
    def setRunVar(runVar = bool):
        DisplayInput.runVar = runVar
    
    def getRunVar():
        return DisplayInput.runVar

class Input:
    class Keyboard:
        def __init__(self):
            pass

        def updateInput():
            if pygame.event.peek() == True:
                for keys in pygame.event.get(pygame.KEYDOWN):
                    match keys.key:
                        case pygame.K_w:
                            print("W")
                        case _: 
                            print("Could not get Input")