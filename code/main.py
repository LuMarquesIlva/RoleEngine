from core import RoleEngine
from input import Input
from objects import Entity, Object

RoleEngine.Init()
x = 6.0
y = 3.0

while Input.getRunVar() == True:
    RoleEngine.Display.Fill(RoleEngine.BG_COLOR)

    keys = Input.Update()
    if keys != None:
        #print(keys)
        pass
    match keys:
        case "W":
            y -= 6.0
        case "A":
            x -= 6.0
        case "S":
            y += 6.0
        case "D":
            x += 6.0
        case _:
            pass

    teste = Object.Rect.createRectObject(0, "Teste", (x, y, 80.0, 80.0))
    Entity.drawRectEntity(teste, (100, 100, 100, 255))

    RoleEngine.Display.Update()

RoleEngine.Quit()