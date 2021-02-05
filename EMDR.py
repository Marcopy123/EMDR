import pygame
import time

pygame.init()

FPS = 160
fpsClock = pygame.time.Clock()

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

pos = [int(WIDTH/2), int(HEIGHT/2)]

YELLOW = (246, 254, 170)
TURQUOISE = (121, 199, 197)
BLACK = (0, 0, 0)

speedOfCircle = 20

radius = 40
numberOfLoops = 0

def moveCircle(screen, backgroundColor, color, position, radius):
    screen.fill(backgroundColor) # fills the screen with black
    pos[0] += speedOfCircle # moves the ball onthe x axis using the speedOfCircle
    ball = pygame.draw.circle(screen, color, position, radius) # draws the circle on the screen, in white, with the new position, and the radius

while not done:
    numberOfLoops += 1
    moveCircle(screen, TURQUOISE, YELLOW, pos, radius)

    if pos[0] <= radius or pos[0] + radius >= WIDTH: # if the ball touched the edges
        speedOfCircle = -speedOfCircle # change the speedOfCircle to -speedOfCircle


    if numberOfLoops >= 800:
        numberOfLoops += 1
        moveCircle(screen, TURQUOISE, YELLOW, pos, radius)
        if pos[0] <= radius or pos[0] + radius >= WIDTH:
            speedOfCircle = -50








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    fpsClock.tick(FPS)


pygame.display.update()
