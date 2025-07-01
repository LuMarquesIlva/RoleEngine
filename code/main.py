from core import RoleEngine
from input import Input

RoleEngine.Init()

Input.setRunVar(True)
while Input.getRunVar() == True:
    Input.Update()
    
    RoleEngine.Display.Update()

RoleEngine.Quit()