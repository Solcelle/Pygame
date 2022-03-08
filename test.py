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
background = pygame.image.load(BG_FNAME).convert()
ball_img = pygame.image.load(BALL_FNAME).convert_alpha()


# Parent for moving objects
class MovingObj():
	def __init__(self):
		self.x = 42
		self.y = 200
		self.speed = [200 + 400 * random.random(), 200 + 400 * random.random()]

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
		pass


# Create ball
class Ball(MovingObj):
	def __init__(self):
		super().__init__()
		self.img = ball_img
		self.width = ball_img.get_width()
		self.height = ball_img.get_height()
		
	def draw(self):
		screen.blit(self.img, (self.x, self.y))

# Create circle
class Circle(MovingObj):
	def __init__(self):
		super().__init__()
		self.radius = 30
		self.width = 30
		self.height = 30
		self.color = (200, 0, 100)

	def draw(self):
		pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.radius)


ball1 = Ball()	# Creates single object

list = [		# Creates multiple objectes
	Ball(),
	Ball(),
	Ball(),
	Ball(),
	Circle(),
	Circle(),
	Circle(),
]

clock = pygame.time.Clock()	# Creates game clock

# Game loop
while True:
	# Checks for events in program
	events = pygame.event.get()			
	for event in events:
		if event.type == pygame.QUIT:	# If quit event, end program
			pygame.quit()
			exit()

	# Sets amount of ticks per second
	time_passed = clock.tick(144) / 1000.0

	# Draw backgound
	screen.blit(background, (0, 0))


	# Move single object
	ball1.move(time_passed)

	# Move multiple objects
	for obj in list:
		obj.move(time_passed)
	
	# Draw single object
	ball1.draw()

	# Draw multiple objects
	for obj in list:
		obj.draw()

	# Update display to show new frame
	pygame.display.update()
