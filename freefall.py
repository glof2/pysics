import assets.physicsmath as physics
import assets.engine as engine
import pygame
import math

# Initializing pygame
pygame.init()

# g of earth is around 9.81m/s2
g = 9.81

# 1 frame in 60 FPS is exactly 0.016666666666666667 seconds
stopat = int(input("Stop at (m): "))
t = physics.timetofall(g, stopat)
timetofinish = round(t / 0.016666666666666667)
framecounter = 0

#

# Meter counter
m_counter = 0

# Defining clock for later fps cap
clock = pygame.time.Clock()
FPS = 60

# Creating a window
WINDOWSIZE = (800, 600)
screen = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Pysics")

# Loading needed images
background = pygame.image.load("assets/images/background.jpg").convert()
ball = pygame.image.load("assets/images/ball.png").convert()
ball.set_colorkey((255, 255, 255))

# Ball variables
speed = 0
falling = True
ballx = 400 - ball.get_width()
bally = 50

# Camera variables
scroll = 0
scrollvalue = 0

# Text
font = pygame.font.SysFont("comicsansms", 24)

# Main loop
while True:
    # Checking events
    engine.events()
    screen.fill((0, 0, 0))

    # Blitting images onto the screen
    engine.infinitebackground(screen, background, -scroll)
    screen.blit(ball, (ballx, bally - scroll))

    # Updating text
    speedtext = font.render(f"Speed: {round(speed, 2)}m/s",
                            True, (0, 0, 255))
    meterstext = font.render(f"Meter: {round(m_counter, 2)}m",
                             True, (0, 0, 255))
    timetext = font.render(f"Time: {round(framecounter/60, 2)}s",
                           True, (0, 0, 255))

    # Blitting text onto the screen
    screen.blit(speedtext, (0, 0))
    screen.blit(meterstext, (0, 30))
    screen.blit(timetext, (0, 60))

    if falling:
        # Frame counter
        framecounter += 1
        # Ball movement
        speed = physics.freefall(g, framecounter/60)
        bally += speed
        # Meter counter
        m_counter = physics.getmeters(g, framecounter/60)

    if math.ceil(m_counter) >= stopat:
        falling = False

    # Camera follow
    scrollvalue = (bally - scroll - 308)
    scroll += scrollvalue

    # Updating the screen
    pygame.display.update()

    # Setting the fps cap
    clock.tick(FPS)
