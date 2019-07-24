# much comment
# is happening

from classes import *
import pygame
from pygame import key

pygame.init()
clock = pygame.time.Clock()

player = Player()
objectives = []
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
player.box.rect.center = (75, 175)
objectives[0].box.rect.center = (75, 275)
screen = pygame.display.set_mode((1024, 720))


def update():
    keys = pygame.key.get_pressed()
    print(keys[23], keys[24])
    if keys[23]:
        player.move(False)
    if keys[24]:
        player.move(True)
    for i in objectives:
        i.handleCollision(player.box.rect)


def render():
    screen.fill(pygame.Color("dark blue"))
    screen.fill(player.box.color, player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)


def main():
    while True:
        clock.tick(60)
        update()
        render()
        pygame.display.flip()


if __name__ == "__main__":
    main()