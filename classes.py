# comment
# other comment

import pygame
import random

class Box:
    def __init__(self):
        self.rect = pygame.Rect(50,50,50,50)
        self.color = pygame.Color("blue")


class Player:
    def __init__(self):
        self.box = Box()


    def move(self, dir):
        if dir is 1:
            self.box.rect.move_ip(2,0)
        if dir is 2:
            self.box.rect.move_ip(-2,0)
        if dir is 3:
            self.box.rect.move_ip(0,-2)
        if dir is 4:
            self.box.rect.move_ip(0,2)


class Objective:
    def __init__(self):
        self.box = Box()


    def handleCollision(self,rect):
        if self.box.rect.colliderect(rect):
            self.boxTeleport()
            return True
        return False

    def boxTeleport(self):
        self.box.rect.center = ((random.randint(0, 1024), random.randint(0, 720)))