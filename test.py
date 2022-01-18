import pygame
import random
pygame.init()

# Create screen
SCREEN_X = 640
SCREEN_Y = 480
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)

# Get images
BG_FNAME = "puppies.jpg"
BALL_FNAME = "ball.png"
background = pygame.image.load(BG_FNAME)
ball_img = pygame.image.load(BALL_FNAME).convert_alpha()


# Create ball
class Ball:
	def __init__(self):
		self.x = 42
		self.y = 200
		self.speed = [200 + 400 * random.random(), 200 + 400 * random.random()]
		self.img = ball_img
		self.width = ball_img.get_width()
		self.height = ball_img.get_height()


	def move(self, time_passed):
		self.x += self.speed[0] * time_passed
		self.y += self.speed[1] * time_passed

		if self.x >= (SCREEN_X - self.width):
			self.speed[0] = -abs(self.speed[0])
		if self.x <= 0:
			self.speed[0] = abs(self.speed[0])
		if self.y >= (SCREEN_Y - self.height):
			self.speed[1] = -abs(self.speed[1])
		if self.y <= 0:
			self.speed[1] = abs(self.speed[0])
		
	def draw(self):
		screen.blit(self.img, (self.x, self.y))

ball1 = Ball()

list = [
	Ball(),
	Ball(),
	Ball()
]

clock = pygame.time.Clock()

# Game loop
while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			exit()

	time_passed = clock.tick(144) / 1000.0

	# Draw backgound
	screen.blit(background, (0, 0))


	# Move ball
	ball1.move(time_passed)

	# Move balls
	for obj in list:
		obj.move(time_passed)
	
	# Draw ball
	ball1.draw()

	# Draw balls
	for obj in list:
		obj.draw()


	pygame.display.update()
