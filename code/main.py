from core import RoleEngine
from input import Input
from objects import Entity, Object

RoleEngine.Init()
x = 6.0

while Input.getRunVar() == True:

    Input.Update()

    if Input.Keyboard.getPressedKeys() != None:
        print(Input.Keyboard.getPressedKeys())
        for key in Input.Keyboard.getPressedKeys():
            if key == "D":
                x += 50.0

    teste = Object.Rect.createRectObject(0, "Teste", (x, 60.0, 160.0, 160.0))
    Entity.drawRectEntity(teste, (100, 100, 100, 255))

    RoleEngine.Display.Update()

RoleEngine.Quit()