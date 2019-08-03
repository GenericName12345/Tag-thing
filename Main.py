# much comment
# is happening

import sys, pygame

from pygame.locals import *

from classes import Box, Objective, Player

import sys, pygame
from pygame.locals import *
from classes import Box, Objective, Player, whiteBox
import random


score = 0
score2 = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024, 720))
player = Player()
player2 = Player()
player.box.rect.center = (996, 690)
whiteBox1 = whiteBox()
whiteBox2 = whiteBox()
whiteBox1.box.rect.center = (260, 80)
whiteBox2.box.rect.center = (660, 80)

objectives = []
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
objectives.append(Objective())
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
    for j in objectives:
        if rect.box.rect.colliderect(j.whiteBox.rect) and rect is not j:
            return True
    return False


count = 0
for i in objectives:
    i.box.rect.center = ((random.randint(0,1024), random.randint(0,720)))
    while collidingWithFriends(i) :
        i.box.rect.center = ((random.randint(0, 1024), random.randint(0, 720)))
    count += 100




def update():
    global score
    global score2
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.box.rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.box.rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player.box.rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player.box.rect.move_ip(0, 5)
    if keys[pygame.K_a]:
        player2.box.rect.move_ip(-5, 0)
    if keys[pygame.K_d]:
        player2.box.rect.move_ip(5, 0)
    if keys[pygame.K_w]:
        player2.box.rect.move_ip(0, -5)
    if keys[pygame.K_s]:
        player2.box.rect.move_ip(0, 5)

    for i in objectives:
        if i.handleCollision(player.box.rect):
            score += 1
        if i.handleCollision(player2.box.rect):
            score2 += 1

    if score == 25:
        render()
        myFont = pygame.font.SysFont("Comic Sans", 100)
        image = myFont.render("Player 1 Wins!", 1, (255, 255, 255, 255))
        screen.blit(image, (250, 200))
        pygame.display.flip()
        try:
            while True:
                pygame.event.pump()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    raise Exception("Yolo")
                pygame.time.delay(10)
        except e:
            pygame.display.quit()

    if score2 == 25:
        render()
        myFont = pygame.font.SysFont("Comic Sans", 100)
        image = myFont.render("Player 2 Wins!", 1, (255, 255, 255, 255))
        screen.blit(image, (250, 200))
        pygame.display.flip()
        try:
            while True:
                pygame.event.pump()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    raise Exception("Yolo")
                pygame.time.delay(10)
        except e:
            pygame.display.quit()


def render():
    screen.fill(pygame.Color("dark blue"))
    screen.fill(player.box.color, player.box.rect)
    screen.fill(player2.box.color, player2.box.rect)
    screen.fill(whiteBox1.box.color, whiteBox1.box.rect)
    screen.fill(whiteBox2.box.color, whiteBox2.box.rect)

    for i in objectives:
        #screen.fill(i.box.color, i.box.rect)
        pygame.draw.circle(screen, i.box.color, i.box.rect.center, i.box.rect.width)

    myFont = pygame.font.SysFont("Comic Sans", 24)
    image = myFont.render("Player 1 Score: " + str(score),1, player.box.color)
    screen.blit(image, (200, 75))

    myFont = pygame.font.SysFont("Comic Sans", 24)
    image = myFont.render("Player 2 Score: " + str(score2),1, player2.box.color)
    screen.blit(image, (600, 75))

def main():
    while True:
        clock.tick(60)
        update()
        render()
        pygame.display.flip()


if __name__ == "__main__":
    main()