# much comment

from classes import *
import pygame

pygame.init()

player = Player()
objectives = []
objectives.append(objective())
objectives.append(objective())
objectives.append(objective())
screen = pygame.display.set_mode(1024,720)

def update():
    for i in objectives:
        i.handleCollisions(player.box.rect)

def render():
    screen.fill(Color(255,255,255,100))
    screen.fill(player.box.color, player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)

def main():
    update()
    render()
    pygame.display.flip()

if __name__ == "__main__":
    main()