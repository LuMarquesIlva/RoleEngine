from core import RoleEngine
from input import UpdateDisplayInput, Input

RoleEngine.Init()

UpdateDisplayInput.setRunVar(True)
while UpdateDisplayInput.runVar:
    UpdateDisplayInput()
    Input.Keyboard()
    
    RoleEngine.Display.Update()

RoleEngine.Quit()