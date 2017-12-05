from pygame import *
import random

delay = 1
done = False

init()
screen = display.set_mode((640, 480))
mouse.set_pos(640, 480)

my_image = image.load('my_image.png')
event.set_grab(1)

while done == False:

	screen.blit(my_image, (0, 0))
	display.update()
	time.delay(delay)

	for e in event.get():
		if e.type == KEYUP:
			if e.key == K_ESCAPE:
				done = True

	if screen.get_at((mouse.get_pos())) == (0, 0, 0):
		done = True

	if screen.get_at((mouse.get_pos())) == (255, 0, 0, 255):
		my_image = image.load('my_image_2.png')
	if screen.get_at((mouse.get_pos())) == (0, 255, 0, 255):
		my_image = image.load('my_image_3.png')
	if screen.get_at((mouse.get_pos())) == (196, 196, 196, 255):
		my_image = image.load('my_image_4.png')
	if screen.get_at((mouse.get_pos())) == (255, 174, 201, 255):
		my_image = image.load('my_image_5.png')
		mouse.set_pos(640, 480)
	if screen.get_at((mouse.get_pos())) == (163, 73, 164, 255):
		my_image = image.load('my_image_6.png')
	if screen.get_at((mouse.get_pos())) == (112, 146, 190, 255):
		mouse.set_pos(640, 480)
	if screen.get_at((mouse.get_pos())) == (129, 1, 65, 255):
		done = True		
		print("You found a way out")

print("You were in the maze, for", time.get_ticks()/1000, "seconds!")


