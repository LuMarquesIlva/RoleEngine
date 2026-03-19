import threading
from code.display import Display
from code.input import Input
from code.objects import Entity, Object
from code.role_core import RoleEngine

import pygame
from pygame_vkeyboard import *

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
    
def consumer(text):
    return text
    
if not pygame.font.get_init():
    pygame.font.init()   
font = pygame.font.Font("font/04B_03__.TTF", 12)
    
layout = VKeyboardLayout(VKeyboardLayout.QWERTY)
layout.size = 5
keyboard = VKeyboard(Display.displaySurface, consumer, layout)

while Input.getRunVar() is True:
    
    keys = Input.Update()
    keyboard.update(pygame.event.get())
    
    
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
                
                draw()
                updateScreen()
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
            if key == "q" or key == "menu":
                Input.setRunVar(False)

        if inputIndex >= 5:
            inputIndex = 0

        if pygame.event.get(pygame.KEYUP):
            Input.Keyboard.keyPress = False

    draw()
    
    rects = keyboard.draw(Display.DISPLAY.get_surface())
    Display.Update(rects)

RoleEngine.Quit()
