import pygame
from constants import *

def main():
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "#000000")
        pygame.display.flip()
        dt = pygame.time.Clock.tick(clock, 60) / 1000


if __name__ == "__main__":
    main()
