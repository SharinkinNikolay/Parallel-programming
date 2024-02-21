import pygame
import math
import threading

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

sun_radius = 50
sun_x = 500
sun_y = 400

planet1_radius = 10
planet2_radius = 15
planet3_radius = 20
planet1_distance = 150
planet2_distance = 250
planet3_distance = 350
planet1_angle = 0
planet2_angle = 0
planet3_angle = 0


def draw_planet(color, radius, distance, angle):
    planet_x = sun_x + distance * math.cos(math.radians(angle))
    planet_y = sun_y + distance * math.sin(math.radians(angle))
    pygame.draw.circle(screen, color, (int(planet_x), int(planet_y)), radius)


running = True
while running:
    screen.fill(BLACK)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), sun_radius)

    threading.Thread(target=draw_planet, args=(BLUE, planet1_radius, planet1_distance, planet1_angle)).start()
    threading.Thread(target=draw_planet, args=(RED, planet2_radius, planet2_distance, planet2_angle)).start()
    threading.Thread(target=draw_planet, args=(GREEN, planet3_radius, planet3_distance, planet3_angle)).start()

    planet1_angle += 1
    planet2_angle += 0.5
    planet3_angle += 0.25

    print(threading.active_count())

    pygame.display.flip()

pygame.quit()
