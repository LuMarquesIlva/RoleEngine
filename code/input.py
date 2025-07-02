import pygame

class Input():
    runVar = bool

    def Update():
        if pygame.event.peek() == True:
            Input.Display.Update()
            Input.Keyboard.Update()
            Input.Joystick.Update()

    class Display:
        def Update():
                for event in pygame.event.get(pygame.QUIT):
                    if event.type == pygame.QUIT:
                        Input.setRunVar(False)
                        break
            
    class Keyboard:
        def Update():
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
                    case pygame.K_f:
                        Input.Mouse.setMousePosition(30, 30)
                    case _: 
                        print("Could not get Input")

    class Joystick:
        Joysticks = []

        def checkForJoysticks():
            Input.Joystick.Joysticks.clear()
            for joys in range(pygame.joystick.get_count()):
                Input.Joystick.Joysticks.append(pygame.joystick.Joystick(joys))
        
        def printJoysticksInfo():
            for joys in Input.Joystick.Joysticks:
                print(f"ID: {joys.get_instance_id()} - Name: {joys.get_name()} - NumberOfButtons: {joys.get_numbuttons()}")

        def Update():
            #if pygame.CONTROLLERDEVICEADDED:
            #    Input.Joystick.checkForJoysticks()
            #    Input.Joystick.printJoysticksInfo()
                
            for joys in Input.Joystick.Joysticks:
                for joysticks in pygame.event.get(pygame.JOYBUTTONDOWN):
                    match joysticks.button:
                        case 0:
                            print("Controller X")
                        case 1:
                            print("Controller Circle")
                        case 2:
                            print("Controller Triangle")
                        case 3:
                            print("Controller Square")
                        case 4:
                            print("Controller L1")
                        case 5:
                            print("Controller R1")
                        case _:
                            print("Invalid Button")
    class Mouse:
        def getMousePosition():
            if pygame.event.peek(pygame.MOUSEMOTION):
                for mouseEventMotion in pygame.event.get(pygame.MOUSEMOTION):
                    return pygame.mouse.get_pos()
        
        def setMousePosition(x = float, y = float):
            pygame.mouse.set_pos(x, y)
                
        def getMouseButtons():
            if pygame.event.peek(pygame.MOUSEBUTTONDOWN):
                for mouseEventButton in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if mouseEventButton.button != None:
                        return mouseEventButton.button
                    else:
                        pass

        def getMouseWheel():
            if pygame.event.peek(pygame.MOUSEWHEEL):
                for mouseEventWheel in pygame.event.get(pygame.MOUSEWHEEL):
                    return mouseEventWheel
    
    def setRunVar(runVar = bool):
        Input.runVar = runVar
    
    def getRunVar():
        return Input.runVar