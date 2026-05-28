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

teste = Rect(0, "Teste", (300, 400, 800.0, 80.0), (200, 200, 200, 100))

teste2 = Rect(1, "Teste2", (600, 600, 100.0, 100.0), (150, 200, 125, 100))

teste3 = Rect(2, "Teste3", (500, 600, 50, 50), (170, 180, 90, 100))

def draw():
    Display.Fill(Display.BG_COLOR) # Limpa a tela com a cor de fundo
    Entity.drawRectEntity(Object.RenderList) # Chama a função para desenhar os objetos <renderizar>
    Display.Update() # Atualiza a tela
    
if not pygame.font.get_init():
    pygame.font.init()
    
    
    
TouchInput = Input.TouchScreen

while Input.getRunVar() is True: # Enquanto RunVar for verdadeira
    touchPos = TouchInput.getTouchPos()
    inputEvents = Input.Update()
        
    if TouchInput.isTouching():
        for x in Object.RenderList:
            if x.isColliding(touchPos):
                x.Obj.centerx = touchPos[0]
                x.Obj.centery = touchPos[1]
                
                Input.TouchScreen.TouchDebug = True
                Input.TouchScreen.printTouchDebug(x)
    
    if teste.isColliding(teste2):
        print("Colidiu")
    
    
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
