# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	# initialize game
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	AsteroidField.containers = (updatable)
	Player.containers = (updatable, drawable)

	field = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
		updatable.update(dt)
		screen.fill("black")

		collided_asteroids = []
		collided_shots = []

		for ast in asteroids:
			for sh in shots:
				if sh.collision(ast):
					collided_asteroids.append(ast)
					collided_shots.append(sh)

		for ast in collided_asteroids:
			ast.split()
		for sh in collided_shots:
			sh.kill()

		for obj in asteroids:
			if obj.collision(player):
				sys.exit("Game over!")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()