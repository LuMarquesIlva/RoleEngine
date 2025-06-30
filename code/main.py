from core import RoleEngine
from input import DisplayInput, Input

RoleEngine.Init()

DisplayInput.setRunVar(True)
while DisplayInput.getRunVar() == True:
    DisplayInput.Update()
    Input.Keyboard.updateInput()
    
    RoleEngine.Display.Update()

RoleEngine.Quit()