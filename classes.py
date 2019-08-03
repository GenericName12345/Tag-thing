# comment
# other comment

import pygame
import random

class Box:
    def __init__(self):
        self.rect = pygame.Rect(15,15,15,15)
        self.color = pygame.Color("blue")


class Player:
    def __init__(self):
        self.box = Box()
        self.box.rect = pygame.Rect(30, 30, 30, 30)
        self.box.color = pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

class whiteBox:
    def __init__(self):
        self.box = Box()
        self.box.rect = pygame.Rect(90, 90, 160, 60)
        self.box.color = pygame.Color(255, 255, 255)


class Objective:
    def __init__(self):
        self.box = Box()



    def handleCollision(self,rect):
        if self.box.rect.colliderect(rect):
            self.boxTeleport()
            return True
        return False

    def boxTeleport(self):
        self.box.rect.center = ((random.randint(0, 1000), random.randint(0, 705)))