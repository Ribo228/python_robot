

import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((640,480))
robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
window.fill ((0,0,0))
for i in range (1,1001):
    window.blit(robot,(randint(0,640),randint(0,480)))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()