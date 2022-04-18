import pygame
import datetime
import math


pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50

def convert_degrees_to_pygame(R,theta):
    y = math.cos(2*math.pi*theta/360)*R
    x = math.sin(2*math.pi*theta/360)*R
    return x+400,-(y-400)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        time_live = datetime.datetime.now()
        second = time_live.second
        minute = time_live.minute
        hour = time_live.hour
        pygame.display.set_caption(f"{hour}:{minute}:{second}")


        display.fill((0, 0, 0))
        pygame.draw.circle(display, (255, 0, 0), (400, 400), 320,4 )
        pygame.draw.circle(display, (255, 0, 0), (400, 400), 10)

        R = 300
        theta = second*(360/60)
        pygame.draw.line(display,(0,0,255),(400,400),convert_degrees_to_pygame(R,theta),2)

        R = 250
        theta = minute+(second/60)*(360/60)
        pygame.draw.line(display, (0, 0, 255), (400,400), convert_degrees_to_pygame(R, theta),4)

        R = 200
        theta = (hour + minute/60 + second / 3600)*(360/12)
        pygame.draw.line(display, (0, 0, 255), (400,400), convert_degrees_to_pygame(R, theta),8)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ =="__main__":
    main()