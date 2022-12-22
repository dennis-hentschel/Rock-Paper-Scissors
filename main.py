import pygame, random

pygame.init()
pygame.display.set_caption("Rock Paper Scissors")
screen_height = 650
screen_width = 650
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_icon(pygame.image.load("img/icon.png"))
clock = pygame.time.Clock()
mps = 14
bg_colour = (0,0,0)

border = 320
step = 20

rock_img = pygame.transform.scale(pygame.image.load("img/rock.png"), (25,25))
paper_img = pygame.transform.scale(pygame.image.load("img/paper.png"), (25,25))
scissors_img = pygame.transform.scale(pygame.image.load("img/scissors.png"), (25,25))

rps = [[],[],[]]

done = False
start_objects_count = 15

class obj:
	def __init__(self, object_type, position):
		global rock_img, paper_img, scissors_img
		self.object_type = object_type
		self.position = position
		switch = {
			"r":rock_img,
			"p":paper_img,
			"s":scissors_img
		}
		self.icon = switch.get(object_type)
	
	def move(self, pos):
		self.position = pos

def draw_screen():
	global rps
	
	screen.fill(bg_colour)

	for i in range(3):
		for j in rps[i]:
			screen.blit(j.icon, (j.position[0] + screen_width/2, j.position[1] + screen_height/2))

	pygame.display.update()

def move():
	global rps
	for i in range(3):
		for j in rps[i]:
			movement = (j.position[0] + random.randrange(-step,step+1,step), j.position[1] + random.randrange(-step,step+1,step))
			if movement[0] < -border: movement = (-border + step, movement[1])
			if movement[0] > border: movement = (border - step, movement[1])
			if movement[1] < -border: movement = (movement[0], -border + step)
			if movement[1] > border: movement = (movement[0], border - step)
			j.move(movement)

def rock_paper_scissors_check(winner, loser):
	switch = {
		("r", "p"): -1,
		("r", "s"): 1,
		("p", "r"): 1,
		("p", "s"): -1,
		("s", "r"): -1,
		("s", "p"): 1
	}
	return switch.get((winner.object_type, loser.object_type), 0)

def handle_collision():
	global rps
	for i in range(3):
		for j in rps[i]:
			for k in range(3):
				for l in rps[k]:
					if j.position == l.position:
						win = rock_paper_scissors_check(j,l)
						if win == 0: break
						if win == 1:
							print(str(j.object_type) + " eats " + str(l.object_type))
							l.object_type = j.object_type
							l.icon = j.icon
						else:
							print(str(l.object_type) + " eats " + str(j.object_type))
							j.object_type = l.object_type
							j.icon = l.icon


def setup():
	global r,p,s

	for i in range(start_objects_count):
		rps[0].append(obj("r", (random.randrange(-border,border,step), random.randrange(-border,border,step))))
	for i in range(start_objects_count):
		rps[1].append(obj("p", (random.randrange(-border,border,step), random.randrange(-border,border,step))))
	for i in range(start_objects_count):
		rps[2].append(obj("s", (random.randrange(-border,border,step), random.randrange(-border,border,step))))

def run():
	move()
	clock.tick(mps/2)
	handle_collision()
	draw_screen()
	clock.tick(mps/2)

setup()
while(not done):
	run()
input()