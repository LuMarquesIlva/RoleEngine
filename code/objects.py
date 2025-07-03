from core import RoleEngine
import pygame

#TODO create and object and entity class with support for easy handling by abstracting

class Object:
    #TODO Create an object system, mainly for GUI, but can be used for non drawable objects,
    # for logic purposes, with support for semi-dinamic, but mostly static objects
    
    class Rect:
        Id = 0
        Name = ""
        x1, y1 = 0.0, 0.0
        x2, y2 = 0.0, 0.0
        RectObject = {
            "ID" : int,
            "Name" : "",
            "Type" : pygame.rect.Rect
        }
        FRectObject = {
            "ID" : int,
            "Name" : "",
            "Type" : pygame.rect.FRect
        }

        def createRectObject(id = int, name = str, area = (float, float, float, float)):
            rect = pygame.rect.Rect(area[0], area[1], area[2], area[3])
            RectObject = Object.Rect.RectObject
            RectObject["ID"] = id
            RectObject["Name"] = name
            RectObject["Type"] = rect
            return RectObject

        def createFRectObject(id = int, name = str, area = (float, float, float, float)):
            fRect = pygame.rect.Rect(area[0], area[1], area[2], area[3])
            FRectObject = Object.Rect.FRectObject
            FRectObject["ID"] = id
            FRectObject["Name"] = name
            FRectObject["Type"] = fRect
            return FRectObject
        
class Entity(Object):
    #TODO Create an entity system that will handle dinamic objects, such as position,
    # rotation, scale, path finding, animations, effect, and general manipulation (lerp, etc...)
    RectObject = Object.Rect.RectObject
    Color = (200, 200, 200, 200)

    def drawRectEntity(rect = RectObject, color = (int, int, int, int)):
        return pygame.draw.rect(RoleEngine.displaySurface, color, rect["Type"])