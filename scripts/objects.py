from scripts.display import Display

import pygame

class Object:
    # TODO Create an object system, mainly for GUI, but can be used for non drawable objects,
    # for logic purposes, with support for semi-dinamic, but mostly static objects
    
    Position = (float, float)
    Rotation = (float, float)
    Scale = (float, float)

    Z = int
    
    RenderList = []
    
    def addToRenderList(self):
        if self.Z <= len(Object.RenderList):
            print(self.Z)
            Object.RenderList.append(self)
        elif self.Z > len(Object.RenderList):
            print("LENGHT" + str(len(Object.RenderList)))
            for Index in range(self.Z-1):
                if Object.RenderList[Index] is None:
                    Object.RenderList.append(None)
                print(Object.RenderList)
                if Index < len(Object.RenderList) and Object.RenderList[Index] == None:
                    Object.RenderList.insert(Index, None)
                else:
                    continue
    
    def isColliding(self, OBJ1):
        if type(OBJ1) == Rect:
            if self.Obj.colliderect(OBJ1.Obj):
                return True
            else:
                return False
        elif type(OBJ1) == tuple:
            OBJ2 = self
            if OBJ1[0] > OBJ2.Obj.left and OBJ1[0] < OBJ2.Obj.right and OBJ1[1] > OBJ2.Obj.top and OBJ1[1] < OBJ2.Obj.bottom:
                return True
            else:
                return False

class Rect(Object):
    X, Y = float, float
    
    ID = int
    Name = ""
    Obj = pygame.rect.Rect
    Color = (float, float, float, float)
    Scale = (float, float)

        
# -------- Construtor --------

    def __init__(self, ID=int, Layer=int, name=str, area=(float, float, float, float), Color=(float, float, float, float)):
        
        self.Position = (area[0], area[1])
        self.Scale = (area[2], area[3])
        
        self.X, self.Y = self.Position[0], self.Position[1]
        
        
        rect = pygame.rect.Rect(self.Position[0], self.Position[1], self.Scale[0], self.Scale[1])
        
        self.ID = ID
        self.Name = name
        self.Obj = rect
        self.Color = Color
        self.Z = Layer
        
        self.addToRenderList()
        
    def __call__(self):
        return self
        
# ----------------------------


class Entity():
    # TODO Create an entity system that will handle dinamic objects, such as position,
    # rotation, scale, path finding, animations, effect, and general manipulation (lerp, etc...)
    
    def drawRectEntity(ObjectsList = list):
        surface = Display.DISPLAY.get_surface()
        for _rect in ObjectsList:
            surface.fill(_rect.Color, _rect.Obj) # Renderiza o Rect através do fill para utilizar aceleração de hardware quando possível
        
