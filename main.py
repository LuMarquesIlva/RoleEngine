#/// script
#!.venv/Scripts/python.exe -S uv run --script
#///

import threading
from scripts.display import Display
from scripts.input import Input
from scripts.objects import Entity, Object
from scripts.role_core import RoleEngine

import pygame

RoleEngine.Init()
velocity = 0.5

eventString = None

def updateScreen():
    screen_thread = threading.Thread(target=Display.Update())
    screen_thread.start()
    screen_thread.join()
    
Input.Joystick.printJoysticksInfo()
Input.Joystick.RemoveJoystickByID(0)

teste = Object.Rect.createRectObject(0, "Teste", (300, 400, 80.0, 80.0))

def draw():
    Display.Fill(Display.BG_COLOR)

    Entity.drawRectEntity(teste, (100, 250, 100, 255))
    Display.Update()
    
if not pygame.font.get_init():
    pygame.font.init()

while Input.getRunVar() is True:
    TouchInput = Input.TouchScreen.getTouchPos()
    
    if TouchInput != None and Input.displayDebugPrint == True:
        print(TouchInput)
        
    if Input.TouchScreen.isTouching():
        
        if Object.isColliding(TouchInput, teste):
            if Input.displayDebugPrint == True:
                print(Object.isColliding(TouchInput, teste))
            teste["RectObject"].centerx = TouchInput[0]
            teste["RectObject"].centery = TouchInput[1]
    
    inputEvents = Input.Update()

    if inputEvents == "q" or inputEvents == "menu" or inputEvents == pygame.QUIT:
        Input.setRunVar(False)
        pygame.quit()
        break

    while inputEvents is not None and type(inputEvents) is str and pygame.event.peek(pygame.KEYUP) == False:
        #print(inputEvents)
        
        try:
            if type(inputEvents) == str:
                eventString = ''.join(inputEvents)
        except TypeError as exc:
             raise exc
        
        for event in inputEvents:
            if eventString is not None:
                match eventString:
                    case 'w':
                        teste["RectObject"].y -= 1 * velocity
                    case 'wd':
                        teste["RectObject"].x += 1 * velocity
                        teste["RectObject"].y -= 1 * velocity
                    case 'a':
                        teste["RectObject"].x -= 1 * velocity
                    case 's':
                        teste["RectObject"].y += 1 * velocity
                    case 'd':
                        teste["RectObject"].x += 1 * velocity
                    case _:
                        pass
        draw()
        continue

    draw()

pygame.quit()
