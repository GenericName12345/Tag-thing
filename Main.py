# much comment
# is happening

import sys, pygame
from pygame.locals import *
from classes import Box, Objective, Player
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024, 720))
player = Player()
player.box.rect.center = (75, 175)
objectives = []
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives[0].box.rect.center = (75, 275)

def collidingWithFriends(rect):
    for i in objectives:
        if rect.box.rect.colliderect(i.box.rect) and rect is not i:
            return True
    return False


count = 0
for i in objectives:
    i.box.rect.center = ((random.randint(0,1024), random.randint(0,720)))
    while collidingWithFriends(i) :
        i.box.rect.center = ((random.randint(0, 1024), random.randint(0, 720)))
    count += 100




def update():
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(2)
    if keys[pygame.K_RIGHT]:
        player.move(1)
    if keys[pygame.K_UP]:
        player.move(3)
    if keys[pygame.K_DOWN]:
        player.move(4)

    for i in objectives:
        i.handleCollision(player.box.rect)
        i.wait()


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