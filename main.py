#/// script
#!.venv/Scripts/python.exe -S uv run --script
#///

from scripts.display import Display
from scripts.input import Input
from scripts.objects import Entity, Object, Rect
from scripts.role_core import RoleEngine

import pygame

RoleEngine.Init()
velocity = 0.5

eventString = None
    
Input.Joystick.printJoysticksInfo()
Input.Joystick.RemoveJoystickByID(0)

teste = Rect(0, 0, "Teste", (10, 10, 90.0, 80.0), (200, 200, 200, 100))

teste2 = Rect(1, 2, "Teste2", (50, 50, 100.0, 100.0), (150, 200, 125, 100))

teste3 = Rect(2, 1, "Teste3", (25, 25, 50, 50), (170, 180, 90, 100))

def draw():
    Display.Fill(Display.BG_COLOR) # Limpa a tela com a cor de fundo
    Entity.drawRectEntity(Object.RenderList) # Chama a função para desenhar os objetos <renderizar>
    Display.Update() # Atualiza a tela
    
if not pygame.font.get_init():
    pygame.font.init()
    
    
TouchInput = Input.TouchScreen

while Input.getRunVar() is True: # Enquanto RunVar for verdadeira
    inputEvents = Input.Update()

    touchPos = TouchInput.getTouchPos()
    mousePos = Input.Mouse.getMousePosition()
        
    if TouchInput.isTouching():
        for x in Object.RenderList:
            if x.isColliding(touchPos):
                x.Obj.centerx = touchPos[0]
                x.Obj.centery = touchPos[1]
                
                Input.TouchScreen.TouchDebug = False
                Input.TouchScreen.printTouchDebug(x)
    
    if Input.Mouse.isPressingButton():
        button1 = Input.Mouse.getMouseButtons(1)

        if button1 == "MouseLeft":
            for x in Object.RenderList:
                if x.isColliding(mousePos):
                    x.Obj.centerx = mousePos[0]
                    x.Obj.centery = mousePos[1]
        
    
    if inputEvents == "q" or inputEvents == "menu" or inputEvents == pygame.QUIT:
        Input.setRunVar(False)
        pygame.quit()
        break

    while inputEvents is not None and type(inputEvents) is str and pygame.event.peek(pygame.KEYUP) == False:
        
        try:
            if type(inputEvents) == str:
                eventString = ''.join(inputEvents)
        except TypeError as exc:
             raise exc
        
        for event in inputEvents:
            if eventString is not None:
                match eventString:
                    case 'w':
                        teste.Obj.y -= 1 * velocity
                    case 'wd':
                        teste.Obj.x += 0.5 * velocity
                        teste.Obj.y -= 0.5 * velocity
                    case 'a':
                        teste.Obj.x -= 1 * velocity
                    case 's':
                        teste.Obj.y += 1 * velocity
                    case 'd':
                        teste.Obj.x += 1 * velocity
                    case _:
                        pass
        draw()
        continue

    draw()

pygame.quit()
