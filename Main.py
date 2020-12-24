# importing necessary modules.
import time
from random import randint
import pygame
from pygame.locals import *
pygame.init()


clock = pygame.time.Clock() # the ingame clock

fps = 60
up = False
down = False
player_location = [250 ,200]
friction = 0.9
force = 0
misy = randint(0, 800)
misy2 = randint(0, 800)
misy3 = randint(0, 800)
hary = randint(0, 800)
cony = randint(0, 800)
missile_loc = [795,misy]
missile_loc2 = [795,misy2]
missile_loc3 = [795,misy3]
hart_loc = [795,hary]
con_loc = [795,cony]
count = 3

player = pygame.image.load("assets/ship.png")
missile = pygame.image.load("assets/missile.png")
heart = pygame.image.load("assets/heart.png")

Window_size = (800,600)
pygame.display.set_caption("PyDodge v0.1 (alpha)")
screen = pygame.display.set_mode(Window_size, 0, 0)

player_rect = pygame.Rect(player_location[0], player_location[1], player.get_width(), player.get_height())

global score
score = 0
global hp
hp = 3

font = pygame.font.Font("assets/Monoid-Retina.ttf", 50)

while count > 0:
	screen.fill((146, 244, 255))
	count_tex = font.render(str(count), True, "Black")
	screen.blit(count_tex, [20, 20])
	pygame.display.update()
	time.sleep(1)
	count -= 1

font = pygame.font.Font("assets/Monoid-Retina.ttf", 20)

go = True
while go:

	screen.fill((146, 244, 255))

	missile_rect = pygame.Rect(missile_loc[0], missile_loc[1], missile.get_width(), missile.get_height())
	missile_rect2 = pygame.Rect(missile_loc2[0], missile_loc2[1], missile.get_width(), missile.get_height())
	missile_rect3 = pygame.Rect(missile_loc3[0], missile_loc3[1], missile.get_width(), missile.get_height())
	hart_rect = pygame.Rect(hart_loc[0], hart_loc[1], 15, 15)
	con_rect = pygame.Rect(con_loc[0], con_loc[1], 15, 15) # coin.get_width(), coin.get_height()

	# pygame.draw.rect(screen, (0,0,0), player_rect)
	# pygame.draw.rect(screen, (255,0,0), missile_rect)
	# pygame.draw.rect(screen, (255,0,0), missile_rect2)
	# pygame.draw.rect(screen, (255,0,0), missile_rect3)
	# pygame.draw.rect(screen, (255,0,0), hart_rect)
	pygame.draw.rect(screen, (255, 255, 0), con_rect)

	score_tex = font.render("Score:"+str(score), True, "Black")
	screen.blit(score_tex, [20,20])
	hp_tex = font.render("HP:"+str(hp), True, "Black")
	screen.blit(hp_tex, [20,560])

	screen.blit(player, player_location)
	screen.blit(missile, missile_loc)
	screen.blit(missile, missile_loc2)
	screen.blit(missile, missile_loc3)
	screen.blit(heart, hart_loc)

	player_rect.x = player_location[0]
	player_rect.y = player_location[1]

	missile_loc[0] -= 8
	missile_loc2[0] -= 7
	missile_loc3[0] -= 9
	hart_loc[0] -= 10
	con_loc[0] -= 8

	if missile_loc[0] < 0:
		score += 1
		misy = randint(0, 600)
		missile_loc = [795,misy]

	if missile_loc2[0] < 0:
		score += 1
		misy2 = randint(0, 600)
		missile_loc2 = [795,misy2]

	if missile_loc3[0] < 0:
		score +=1
		misy3 = randint(0, 600)
		missile_loc3 = [795,misy3]

	if hart_loc[0] < 0:
		hary = randint(0, 600)
		hart_loc = [795,hary]

	if con_loc[0] < 0:
		cony = randint(0, 600)
		con_loc = [795,cony]

	if player_location[1] > 600:
		player_location[1] = 0

	if player_location[1] < 0:
		player_location[1] = 600
 
	player_location[1] += force

	force *= friction

	if up == True:
		force -= 0.8
	if down == True:
		force += 0.8

	if player_rect.colliderect(missile_rect):
		hp -= 1
		misy = randint(0, 600)
		missile_loc = [795,misy]

	if player_rect.colliderect(missile_rect2):
		hp -= 1
		misy2 = randint(0, 600)
		missile_loc2 = [795,misy2]

	if player_rect.colliderect(missile_rect3):
		hp -= 1
		misy3 = randint(0, 600)
		missile_loc3 = [795,misy3]

	if player_rect.colliderect(hart_rect):
		hp += 1
		hary = randint(0, 600)
		hart_loc = [795,hary]

	if player_rect.colliderect(con_rect):
		score += 5
		cony = randint(0, 600)
		con_loc = [795,cony]

	if hp == 0:
		font = pygame.font.Font("assets/Monoid-Retina.ttf", 40)
		screen.fill((146, 244, 255))
		game_tex = font.render("GAME OVER", True, "Black")
		screen.blit(game_tex, [20, 20])
		screen.blit(score_tex, [20, 300])
		pygame.display.update()
		time.sleep(3)
		go = False

	for event in pygame.event.get():
		if event.type == QUIT:
			go = False
		if event.type == KEYDOWN:
			if event.key == K_UP:
				up = True
			if event.key == K_DOWN:
				down = True
		if event.type == KEYUP:
			if event.key == K_UP:
				up = False
			if event.key == K_DOWN:
				down = False

	pygame.display.update()
	clock.tick(fps)

pygame.quit()