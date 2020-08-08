import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 650, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de naves")

YELLOW_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.ship_img = None


	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
	def __int__(self, x, y):
		super().__init__(x, y)
		self.ship_img = YELLOW_SHIP


def main():
	run = True
	FPS = 60
	nivel = 1
	vidas = 5

	main_font = pygame.font.SysFont("comicsans", 40)

	clock = pygame.time.Clock()

	player_vel = 5
	player = Player(300, 550)

	def redraw_windows():
		WIN.blit(BG, (0,0))
		nivel_label = main_font.render("Nivel : " + str(nivel), 1, (255, 255, 255))
		WIN.blit(nivel_label, (10,10))
		vidas_label = main_font.render("Vidas : " + str(vidas), 1, (255, 255, 255))
		WIN.blit(vidas_label, (WIDTH - vidas_label.get_width() - 10, 10))

		player.draw(WIN)
		pygame.display.update()


	while run:
		clock.tick(FPS)
		redraw_windows()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player_vel > 0:	# move left
			player.x -= player_vel
		if keys[pygame.K_d] and player.x + player_vel + 50 < WIDTH:	# move right
			player.x += player_vel
		if keys[pygame.K_w] and player.y - player_vel > 0:	# move up
			player.y -= player_vel
		if keys[pygame.K_s] and player.y + player_vel + 50 < HEIGHT:	# move down
			player.y += player_vel


main()