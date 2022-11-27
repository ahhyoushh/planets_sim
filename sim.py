import sys
import pygame
import math



WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planets SIM!")

# COLORS
YELLOW = (255, 255, 2)
BLUE = (100, 149, 237)
RED =  (188, 39, 50)
DARK_GREY = (80, 78, 81)
WHITE = (255, 255, 255)
class Planet:

    AU  = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 150 / (AU) # CHange /2 #AU = 100px
    TIMESTEP = 3600*24 


    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

pygame.init()
def main():
    run = True
    clock = pygame.time.Clock()
    pygame.display.update()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24 )

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)

    venus = Planet(0.732 * Planet.AU, 0, 13, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        run = True
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()
    sys.exit(0)


main()