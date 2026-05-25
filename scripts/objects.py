from scripts.display import Display

import pygame

# TODO create and object and entity class with support for easy handling by abstracting


class Object:
    # TODO Create an object system, mainly for GUI, but can be used for non drawable objects,
    # for logic purposes, with support for semi-dinamic, but mostly static objects
    
    def isColliding(OBJ1, OBJ2):
        if type(OBJ1) == Object:
            if OBJ1.RectObject[2].colliderect(OBJ2):
                return True
            else:
                return False
        elif type(OBJ1) == tuple:
            if OBJ1[0] > OBJ2["RectObject"].left and OBJ1[0] < OBJ2["RectObject"].right and OBJ1[1] > OBJ2["RectObject"].top and OBJ1[1] < OBJ2["RectObject"].bottom:
                return True
            else:
                return False

    class Rect:
        Id = 0
        Name = ""
        RectObject = {"ID": int, "Name": "", "Type": pygame.rect.Rect}

        def createRectObject(id=int, name=str, area=(float, float, float, float)):
            RectObject = Object.Rect.RectObject

            rect = pygame.rect.Rect(area[0], area[1], area[2], area[3])
            RectObject["ID"] = id
            RectObject["Name"] = name
            RectObject["RectObject"] = rect
            return RectObject


class Entity(Object):
    # TODO Create an entity system that will handle dinamic objects, such as position,
    # rotation, scale, path finding, animations, effect, and general manipulation (lerp, etc...)
    RectObject = Object.Rect.RectObject
    Color = (200, 200, 200, 200)

    def drawRectEntity(rect=RectObject, color=(int, int, int, int)):
        return pygame.draw.rect(Display.displaySurface, color, rect["RectObject"])
