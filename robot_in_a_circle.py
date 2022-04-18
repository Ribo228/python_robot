import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2
    window.fill((0, 0, 0))
    for i in range(1, 11):
        window.blit(robot, (x*i, y*i))
        pygame.display.flip()

    angle += 0.01
    clock.tick(60)