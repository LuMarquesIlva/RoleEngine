import pygame

class Input():
    runVar = bool

    def Update():
        if pygame.event.peek() == True:
            Input.Display.Update()
            Input.Joystick.Update()
            key = Input.Keyboard.Update()
        return key

    class Display:
        def Update():
                for event in pygame.event.get(pygame.QUIT):
                    if event.type == pygame.QUIT:
                        Input.setRunVar(False)
                        break
            
    class Keyboard:
        keyPress = False

        def Update():
            #print(pygame.event.get(pygame.KEYDOWN))
            for keys in pygame.event.get(pygame.KEYDOWN):
                Input.Keyboard.keyPress = True
                while Input.Keyboard.keyPress == True:
                    match keys.key:
                        case pygame.K_w:
                            return "W"
                        case pygame.K_a:
                            return "A"
                        case pygame.K_s:
                            return "S"
                        case pygame.K_d:
                            print(Input.Keyboard.keyPress)
                            return "D"
                        case pygame.K_f:
                            return "F"
                        case _: 
                            print("Could not get Input")
            if Input.Keyboard.keyPress == True and pygame.event.get(pygame.KEYUP):
                Input.Keyboard.keyPress = False
                print('FUnciona')
            else:
                Input.Keyboard.keyPress = True
        
        #TODO Figure out a way to get the pressed keys with a single function
        def getPressedKeys():
            keys = []
            key = Input.Keyboard.Update()

            if keys != None:
                keys.append(key)
                for Keys in keys:
                    return Keys
            else:
                pass

    class Joystick:
        Joysticks = []
        controllerCheckingIndex = 0

        def checkForJoysticks():
            Input.Joystick.Joysticks.clear()
            for joys in range(pygame.joystick.get_count()):
                Input.Joystick.Joysticks.append(pygame.joystick.Joystick(joys))
            
            if Input.Joystick.controllerCheckingIndex >= 3:
                Input.Joystick.controllerCheckingIndex = 0
        
        def printJoysticksInfo():
            for joys in Input.Joystick.Joysticks:
                print(f"ID: {joys.get_instance_id()} - Name: {joys.get_name()}")

        def Update():
            #print(pygame.event.get())
            try:
                for device in pygame.event.get(pygame.JOYDEVICEADDED) or pygame.event.get(pygame.JOYDEVICEREMOVED):
                    if Input.Joystick.controllerCheckingIndex < 4 and device.type == pygame.JOYDEVICEADDED:
                        Input.Joystick.checkForJoysticks()
                        Input.Joystick.printJoysticksInfo()
                        Input.Joystick.controllerCheckingIndex += 1
                    elif Input.Joystick.controllerCheckingIndex < 4 and device.type == pygame.JOYDEVICEREMOVED:
                        Input.Joystick.checkForJoysticks()
                        print("Device Removed")
                        Input.Joystick.controllerCheckingIndex += 1
            except:
                print("-- Error detecting joystick -- Tried 3 Times --")

            for joys in Input.Joystick.Joysticks:
                for joyButton in pygame.event.get(pygame.JOYBUTTONDOWN):
                    match joyButton.button:
                        case 0:
                            print(f"Controller {joyButton.joy} X")
                        case 1:
                            print(f"Controller {joyButton.joy} Circle")
                        case 2:
                            print(f"Controller {joyButton.joy} Square")
                        case 3:
                            print(f"Controller {joyButton.joy} Triangle")
                        case 4:
                            print(f"Controller {joyButton.joy} L1")
                        case 5:
                            print(f"Controller {joyButton.joy} R1")
                        case 6:
                            print(f"Controller {joyButton.joy} Select")
                        case 7:
                            print(f"Controller {joyButton.joy} Start")
                        case 8:
                            print(f"Controller {joyButton.joy} L3")
                        case 9:
                            print(f"Controller {joyButton.joy} R3")
                        case 10:
                            print(f"Controller {joyButton.joy} Home")
                        case 11:
                            print(f"Controller {joyButton.joy} idk")
                        case _:
                            print("Invalid Button")
                    
                for joyHat in pygame.event.get(pygame.JOYHATMOTION):
                    match joyHat.value:
                        case (1, 0):
                            print(f"Controller {joyHat.joy} Hat Right")
                        case (-1, 0):
                            print(f"Controller {joyHat.joy} Hat Left")
                        case (0, 1):
                            print(f"Controller {joyHat.joy} Hat Up")
                        case (0, -1):
                            print(f"Controller {joyHat.joy} Hat Down")
                
                for joyAxis in pygame.event.get(pygame.JOYAXISMOTION):
                    match joyAxis.axis:
                        case 0:
                            print(f"Controller {joyAxis.joy} Left Analog V: Value {joyAxis.value}")
                        case 1:
                            print(f"Controller {joyAxis.joy} Left Analog H: Value {joyAxis.value}")
                        case 2:
                            print(f"Controller {joyAxis.joy} Right Analog V: Value {joyAxis.value}")
                        case 3:
                            print(f"Controller {joyAxis.joy} Right Analog H: Value {joyAxis.value}")
                        case 4:
                            print(f"Controller {joyAxis.joy} L2: Value {joyAxis.value}")
                        case 5:
                            print(f"Controller {joyAxis.joy} R2: Value {joyAxis.value}")
                
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