# comment
# other comment

import pygame

class Box:
    def __init__(self):
        self.rect = pygame.Rect(50,50,50,50)
        self.color = pygame.Color("red")


    def colorChange(self):
        self.color = pygame.Color(255,0,0,100)


class Player:
    def __init__(self):
        self.box = Box()


    def move(self, dir):
        if dir is True:
            self.box.rect.move_ip(2,0)
        else:
            self.box.rect.move_ip(-2,0)


class Objective:
    def __init__(self):
        self.box = Box()


    def handleCollision(self,rect):
        if self.box.rect.colliderect(rect):
            self.box.colorChange()