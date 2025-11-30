import threading
from code.display import Display
from code.input import Input
from code.objects import Entity, Object
from code.role_core import RoleEngine

import pygame

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


while Input.getRunVar() is True:
    keys = Input.Update()
    if keys is not None:
        print(keys)

    inputIndex = 0
    while Input.Keyboard.keyPress and keys is not None:
        for key in keys:
            if key == "w":
                y -= 1.0
                if key == "d":
                    x += 1.0
                elif key == "a":
                    x -= 1.0
                updateScreen()
                draw()
            if key == "a":
                x -= 1.0
                if key == "w":
                    y -= 1.0
                elif key == "s":
                    y += 1.0
                updateScreen()
                draw()
            if key == "s":
                y += 1.0
                if key == "d":
                    x += 1.0
                elif key == "a":
                    x -= 1.0
                updateScreen()
                draw()
            if key == "d":
                x += 1.0
                if key == "w":
                    y -= 1.0
                elif key == "s":
                    y += 1.0
                updateScreen()
                draw()
            if key == "q":
                Input.setRunVar(False)

        if inputIndex >= 5:
            inputIndex = 0

        if pygame.event.get(pygame.KEYUP):
            Input.Keyboard.keyPress = False

    draw()

    Display.Update()

RoleEngine.Quit()
