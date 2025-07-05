from role_core import RoleEngine
from input import Input
from objects import Entity, Object
from display import Display
import pygame
import threading

RoleEngine.Init()
x = 300.0
y = 400.0

def updateScreen():
    screen_thread = threading.Thread(target=Display.Update())
    screen_thread.start()
    screen_thread.join()

def draw():
    Display.Fill(Display.BG_COLOR)

    teste = Object.Rect.createRectObject(0, "Teste", (x, y, 80.0, 80.0))
    Entity.drawRectEntity(teste, (100, 250, 100, 255))

while Input.getRunVar() == True:

    keys = Input.Update()
    if keys != None:
        print(keys)

    inputIndex = 0
    while Input.Keyboard.keyPress == True and keys != None:
        match keys:
            case "W":
                y -= 1.0
                updateScreen()
                draw()
            case "A":
                x -= 1.0
                updateScreen()
                draw()
            case "S":
                y += 1.0
                updateScreen()
                draw()
            case "D":
                x += 1.0
                updateScreen()
                draw()
            case _:
                pass
        
        if inputIndex >= 5:
            inputIndex = 0
        
        if pygame.event.get(pygame.KEYUP):
            Input.Keyboard.keyPress = False
    
    draw()

    Display.Update()

RoleEngine.Quit()