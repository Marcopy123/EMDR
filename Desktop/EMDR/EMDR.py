import pygame
import time

pygame.init()

FPS = 120
fpsClock = pygame.time.Clock()

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

pos = [int(WIDTH/2), int(HEIGHT/2)]

ballColor = (42, 68, 148)
backgroundColor = (121, 199, 197)


speedOfCircle = 50

radius = 50
numberOfLoops = 0

def moveCircle(screen, backgroundColor, color, position, radius):
    pos[0] += speedOfCircle # moves the ball onthe x axis using the speedOfCircle
    screen.fill(backgroundColor) # fills the screen with black
    ball = pygame.draw.circle(screen, color, position, radius) # draws the circle on the screen, in white, with the new position, and the radius

while not done:
    numberOfLoops += 1
    moveCircle(screen, backgroundColor, ballColor, pos, radius)

    if pos[0] <= radius or pos[0] + radius >= WIDTH: # if the ball touched the edges
        speedOfCircle = -speedOfCircle # change the speedOfCircle to -speedOfCircle


    if numberOfLoops >= 800:
        moveCircle(screen, backgroundColor, ballColor, pos, radius)
        if pos[0] <= radius or pos[0] + radius >= WIDTH:
            speedOfCircle = -60

       





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    fpsClock.tick(FPS)


pygame.display.update()