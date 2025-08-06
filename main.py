import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for meteor in asteroids:
            if meteor.collides_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
        for meteor in asteroids:
            for shot in shots:
                if meteor.collides_with(shot):
                    meteor.split()
                    shot.kill()
                    score += 1
        pygame.Surface.fill(screen, "#000000")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock.tick(clock, 60) / 1000


if __name__ == "__main__":
    main()
