import pygame

class Input():
    runVar = bool

    def Update():

        if pygame.event.peek() == True:
            for event in pygame.event.get(pygame.QUIT):
                if event.type == pygame.QUIT:
                    Input.setRunVar(False)
                    break

            for keys in pygame.event.get(pygame.KEYDOWN):
                    match keys.key:
                        case pygame.K_w:
                            print("W")
                        case pygame.K_a:
                            print("A")
                        case pygame.K_s:
                            print("S")
                        case pygame.K_d:
                            print("D")
                        case _: 
                            print("Could not get Input")
    
    def setRunVar(runVar = bool):
        Input.runVar = runVar
    
    def getRunVar():
        return Input.runVar