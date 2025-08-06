import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def exit_game(score, seconds):
    print(f"Scored {score} in {seconds} seconds")
    pygame.quit()
    sys.exit()
    return

def main():
    pygame.init()
    start_ticks = pygame.time.get_ticks()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)
    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("assets/background_galaxy.jpg").convert()
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
            exit_game(score, seconds)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game(score, seconds)
        updatable.update(dt)
        for meteor in asteroids:
            if meteor.collides_with(player):
                print("Game over!")
                exit_game(score, seconds)
        for meteor in asteroids:
            for shot in shots:
                if meteor.collides_with(shot):
                    meteor.split()
                    shot.kill()
                    score += 1
        # pygame.Surface.fill(screen, "#000000")
        screen.blit(background, (0, 0))
        for object in drawable:
            object.draw(screen)
        score_text = font.render(f"Score: {score}", True, WHITE)
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        timer_text = font.render(f"Time: {seconds}s", True, WHITE)
        screen.blit(score_text, (10, 10))  # top left edge of the screen
        screen.blit(timer_text, (10, 40))  # Slightly below the score
        pygame.display.flip()
        dt = pygame.time.Clock.tick(clock, 60) / 1000

if __name__ == "__main__":
    main()
