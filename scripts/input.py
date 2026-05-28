from scripts.display import Display as DP
from scripts.objects import Rect

import pygame

class Input:
    runVar = bool
    
    displayDebugPrint = False

    def Update(): # Função Update Geral

        # A primeira coisa que acontece é checar se um evento de saída foi acionado
        if pygame.event.peek(pygame.QUIT):
            quitEvent = Input.Display.Update()

            if quitEvent is not None:
                return quitEvent

        # Checa se existe eventos de "pygame.KEYDOWN" ou tecla sendo pressionada
        if pygame.event.peek(pygame.KEYDOWN):
            keys = Input.Keyboard.getPressedKeys() # Pega as teclas pressionadas e coloca na variável "keys"
            if keys is not None: # E retorna apenas se não for um valor nulo
                return keys
            Input.Display.Update() # Atualiza a janela de qualquer forma

        # Se um controle acionou um event "JOYBUTTONDOWN" ou "JOYSAXISMOTION"
        if pygame.event.peek(pygame.JOYBUTTONDOWN) or pygame.event.peek(pygame.JOYAXISMOTION):
            joys = Input.Joystick.Update() # Consegue os eventos e coloca na variável joys
            if joys is not None: # Retorna se não for um valor nulo
                return joys
            Input.Display.Update()

    # Classe display: Funções da janela
    class Display:
        def Update():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.QUIT

    # Classe Keyboard: Funções do Teclado
    class Keyboard:
        keyPress = False # Essa variável precisa ser inicializada como false para uso posterior

        def Update(): # Atualiza os eventos do Teclado
            for keys in pygame.event.get(pygame.KEYDOWN): # Para cada evento de tecla retorna como keys
                Input.Keyboard.keyPress = True # Aciona o estado de pressionamento de tecla
                if keys is not None: # Retorna a tecla <keys.key> se não for nulo 
                    return pygame.key.name(keys.key)

            if pygame.event.get(pygame.KEYUP): # Se a tecla for "despressionada"
                Input.Keyboard.keyPress = False # Desativa o estado de pressionamento de tecla
            else:
                pass

        # TODO Figure out a way to get the pressed keys with a single function
        # Função que retorna uma lista de teclas pressionadas
        def getPressedKeys() -> list:
            ind = 0 # Indice
            time = 0 # Tempo
            keys = [] # Lista de teclas
            lastKey = None # Ultima tecla

            while pygame.key.get_pressed(): # Enquanto houver eventos de pressionamento de tecla
                key = Input.Keyboard.Update()
                
                if key != lastKey and key != None: # Se a tecla for diferente da ultima tecla e não for nulo
                    keys.append(key) # Adiciona a tecla no final da lista <keys>
                    pygame.time.wait(120) # Espera 120 milésimos
                if ind >= 2: # Se o indice for maior que dois, ou seja, tem três teclas na lista
                    return keys # Retorna
                lastKey = key
                ind += 1
                time += 1
            else:
                if keys[1] is not None:
                    pass

    # Classe Joystick: Funções do controle
    class Joystick:
        printJoyValues = False
        Joysticks = [] # Lista de controles
        controllerCheckingIndex = 0 # Quantidade de controles

        # Remove o Controle por ID
        def RemoveJoystickByID(ID=int):
            if len(Input.Joystick.Joysticks) > 0:
                remDevice = Input.Joystick.Joysticks.pop(ID) # Utiliza a funçao padrão de lista <pop> para retornar as informações do controle para feedback visual
                print(f"Removed {remDevice.get_name()}\n")

        # Checa por controles
        def checkForJoysticks():
            Input.Joystick.Joysticks.clear() # Limpa a lista
            for joys in range(pygame.joystick.get_count()): # Utiliza o próprio pygame para obter a quantidade de controles conectados
                Input.Joystick.Joysticks.append(pygame.joystick.Joystick(joys)) # Adiciona eles no final da lista

            if Input.Joystick.controllerCheckingIndex >= 3: # Limitador da quantidade de controles
                Input.Joystick.controllerCheckingIndex = 0

        # Imprime as informações de todos os controles
        def printJoysticksInfo():
            for joys in Input.Joystick.Joysticks:
                print(f"-- Joysticks --\nID: {joys.get_instance_id()} - Name: {joys.get_name()}\n")

        # Atualiza as entradas dos controles
        def Update():
            initInd = 0
            if initInd == 0:
                Input.Joystick.checkForJoysticks()
                initInd += 1
            try:    
                # Se houver um evento de controle conectado
                for device in pygame.event.get(
                    pygame.JOYDEVICEADDED
                ) or pygame.event.get(pygame.JOYDEVICEREMOVED):
                    if (
                        Input.Joystick.controllerCheckingIndex < 4
                        and device.type == pygame.JOYDEVICEADDED
                    ):
                        Input.Joystick.checkForJoysticks()
                        Input.Joystick.printJoysticksInfo()
                        Input.Joystick.controllerCheckingIndex += 1
                    elif (
                        Input.Joystick.controllerCheckingIndex < 4
                        and device.type == pygame.JOYDEVICEREMOVED
                    ):
                        Input.Joystick.checkForJoysticks()
                        print("Device Removed")
                        Input.Joystick.controllerCheckingIndex += 1
            except:
                print("-- Error detecting joystick -- Tried 3 Times --")

            # Para cada evento de botão pressionado
            for joys in Input.Joystick.Joysticks:
                for joyButton in pygame.event.get(pygame.JOYBUTTONDOWN):
                    match joyButton.button:
                        case 0:
                           if Input.Joystick.printJoyValues == True:
                               print(f"Controller {joyButton.joy} X")
                           return joyButton.joy
                        case 1:
                            print(f"Controller {joyButton.joy} Circle")
                        case 2:
                            print(f"Controller {joyButton.joy} Square")
                            return  joyButton.joy
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
                            return joyButton.joy
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

                # Para cada evento do D-Pad
                for joyHat in pygame.event.get(pygame.JOYHATMOTION):
                    match joyHat.value:
                        case (1, 0):
                            print(f"Controller {joyHat.joy} Hat Right")
                            return joyHat.joy
                        case (-1, 0):
                            print(f"Controller {joyHat.joy} Hat Left")
                            return joyHat.joy
                        case (0, 1):
                            print(f"Controller {joyHat.joy} Hat Up")
                            return joyHat.joy
                        case (0, -1):
                            print(f"Controller {joyHat.joy} Hat Down")
                            return joyHat.joy

                # Para cada evento do analógico esquerdo e direito e R2 e L2 com botão sensivel
                for joyAxis in pygame.event.get(pygame.JOYAXISMOTION):
                    match joyAxis.axis:
                        case 0:
                            if Input.displayDebugPrint == True:
                                print(f"Controller {joyAxis.joy} Left Analog V: Value {joyAxis.value}")
                            return joyAxis.value
                        case 1:
                            if Input.displayDebugPrint == True:
                                print(
                                f"Controller {joyAxis.joy} Left Analog H: Value {joyAxis.value}"
                            )
                            return joyAxis.value
                        case 2:
                            if Input.displayDebugPrint == True:
                                print(
                                f"Controller {joyAxis.joy} Right Analog V: Value {joyAxis.value}"
                            )
                            return joyAxis.value
                        case 3:
                            if Input.displayDebugPrint == True:
                                print(
                                f"Controller {joyAxis.joy} Right Analog H: Value {joyAxis.value}"
                            )
                            return joyAxis.value
                        case 4:
                            if Input.displayDebugPrint == True:
                                print(f"Controller {joyAxis.joy} L2: Value {joyAxis.value}")
                            return joyAxis.value
                        case 5:
                            if Input.displayDebugPrint == True:
                                print(f"Controller {joyAxis.joy} R2: Value {joyAxis.value}")
                            return joyAxis.value
    # Classe Mouse: Funcções do Mouse
    class Mouse:
        # Consegue a posição do mouse e retorna
        def getMousePosition():
            if pygame.event.peek(pygame.MOUSEMOTION): # Se houver um evento de movimento do mouse
                for mouseEventMotion in pygame.event.get(pygame.MOUSEMOTION):
                    return pygame.mouse.get_pos() # Retorna a posição

        # Modifica a posição do mouse
        def setMousePosition(x=float, y=float):
            pygame.mouse.set_pos(x, y)

        # Consegue os botões do mouse e retorna se não for nulo
        def getMouseButtons():
            if pygame.event.peek(pygame.MOUSEBUTTONDOWN):
                for mouseEventButton in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    if mouseEventButton.button != None:
                        return mouseEventButton.button
                    else:
                        pass

        # Retorna a entrada da roda do mouse
        def getMouseWheel():
            if pygame.event.peek(pygame.MOUSEWHEEL):
                for mouseEventWheel in pygame.event.get(pygame.MOUSEWHEEL):
                    return mouseEventWheel
    
    # Classe TouchScreen
    class TouchScreen:
        x, y = 0.0, 0.0 # Posição
        position = (x, y)
        TouchDebug = False # Debug
        
        def printTouchDebug(x = Rect):
            if Input.TouchScreen.TouchDebug is True:
                print(f"{x.ID} -> {x.Name} {x.Obj.x} | {x.Obj.y}")
        
        def isTouching(): # Retorna se o usuário está tocando na tela
            if pygame.event.peek(pygame.FINGERDOWN, pygame.FINGERMOTION):
                return True
            elif pygame.event.peek(pygame.FINGERUP):
                return False
        
        def getTouchPos(): # Retorna a posição do toque
            if pygame.event.peek(pygame.FINGERDOWN) or pygame.event.peek(pygame.FINGERMOTION):
                for TouchEvent in pygame.event.get(pygame.FINGERMOTION, pygame.FINGERDOWN):
                    x = TouchEvent.x * pygame.display.Info().current_w
                    y = TouchEvent.y * pygame.display.Info().current_h
                
                    return (x, y)
                

    # Modifica a variável de execução
    def setRunVar(runVariable=bool):
        Input.runVar = runVariable

    # Consegue a variável de execução
    def getRunVar():
        return Input.runVar
