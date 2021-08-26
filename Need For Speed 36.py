import pygame
import time
import random 

pygame.init()
display_width = 1600
display_height = 1000

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)

car_width = 78
car_height = 200
pause = False
points = 0

gamedisplays = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Need For Speed 36")
clock = pygame.time.Clock()

carImg = pygame.image.load("player.png")
roadImg = pygame.image.load("road.png")
crash_img = pygame.image.load("crash.png")
road_left = pygame.image.load("roadsideL.png")
road_right = pygame.image.load("roadsideR.png")
Background = pygame.image.load("Background.png")
icon = pygame.image.load("trophy2.png")
T_img = pygame.image.load("trophy1.png") 
inBack = pygame.image.load("Background1.png")
subBack = pygame.image.load("Background2.png")

def introloop():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.display.set_icon(icon)
		gamedisplays.blit(Background,(0,0))
		gamedisplays.blit(T_img,(100,200))
		message_display_I("NEED FOR SPEED 36",100,display_width/2,100)
		Buttons("Play",300,800,100,50,green,yellow,"go")
		Buttons("Exit",1200,800,100,50,red,yellow,"exit")
		Buttons("Instructions",600,800,300,50,blue,yellow,"rules")
		pygame.display.update()
		clock.tick(50)

def Buttons(text,x,y,w,h,bc,ac,Act=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x < mouse[0] < x+w and y < mouse[1] < y+h:
		pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
		message_display(text,40,x+w/2,y+h/2)
		if click[0]==1 and Act!=None:
			if Act=="go":
				countdown()
			elif Act=="exit":
				pygame.quit()
				quit()
			elif Act=="rules":
				instructions()
			elif Act=="back":
				introloop()
			elif Act=="pause":
				paused()
			elif Act=="unpause":
				unpaused()	
	else:
		pygame.draw.rect(gamedisplays,bc,(x,y,w,h))
		message_display(text,40,x+w/2,y+h/2)		
		
def instructions():
	instruct = True
	while instruct:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()	
				quit()
		gamedisplays.blit(inBack,(0,0))
		message_display_I("This is an car game where you have to dodge the incoming cars",40,700,300)	
		message_display_I("INSTRUCTIONS",100,700,100)
		message_display_I("CONTROLS",80,700,400)
		message_display_I("Arrow Left : Move Left",40,300,500)
		message_display_I("Arrow Right : Move Right",40,300,600)		
		message_display_I("Accelerator : A",40,300,700)			
		message_display_I("Brake : D",40,300,800)
		Buttons("Back",1000,800,100,50,blue,yellow,"back")
		pygame.display.update()
		clock.tick(30)

def paused():
	global pause
	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()	
				quit()
		gamedisplays.blit(inBack,(0,0))	
		message_display_I("PAUSED",100,800,250)
		Buttons("Continue",650,500,250,50,green,yellow,"unpause")
		Buttons("Restart",650,700,200,50,blue,yellow,"go")
		Buttons("Main Menu",650,900,350,50,red,yellow,"back")
		pygame.display.update()
		clock.tick(30)

def unpaused():
	global pause
	pause = False

def countdown_background():

	font = pygame.font.Font("freesansbold.ttf",50)
	gamedisplays.blit(roadImg,(300,0))
	gamedisplays.blit(roadImg,(300,-1000))
	gamedisplays.blit(road_left,(0,0))
	gamedisplays.blit(road_left,(0,-1000))
	gamedisplays.blit(road_right,(1300,0))
	gamedisplays.blit(road_right,(1300,-1000))
	car(((display_width / 2) - (car_width / 2)),(display_height - car_height))	
	text = font.render("Passed: 0",True,black)
	score = font.render("Score: 0",True,red)
	gamedisplays.blit(text,(0,50))
	gamedisplays.blit(score,(0,0))
	Buttons("Pause",1450,0,150,50,blue,yellow,"pause")

def countdown():
	countdown = True
	while countdown:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()	
				quit()
		countdown_background()
		message_display_III("3",120,display_width/2,display_height/2)
		pygame.display.update()
		clock.tick(1)
		countdown_background()
		message_display_III("2",120,display_width/2,display_height/2)
		pygame.display.update()
		clock.tick(1)
		countdown_background()
		message_display_III("1",120,display_width/2,display_height/2)
		pygame.display.update()
		clock.tick(1)
		countdown_background()
		message_display_III("LETS GO !!!!",120,display_width/2,display_height/2)
		pygame.display.update()
		clock.tick(1)
		gameloop()
			
def again():
	again = True
	while again:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()	
				quit()
		gamedisplays.blit(subBack,(0,0))
		message_display_II("YOUR SCORE: "+str(points),120,display_width/2,display_height/2)	
		Buttons("Restart",300,800,300,50,blue,yellow,"go")
		Buttons("Exit",1200,800,100,50,red,yellow,"back")
		pygame.display.update()
		clock.tick(30)
	
def obstacle(obs_start_x,obs_start_y,obs):
	if obs==0:
		obs_pic=pygame.image.load("car1.png")
	if obs==1:
		obs_pic=pygame.image.load("car2.png")
	if obs==2:
		obs_pic=pygame.image.load("car3.png")
	if obs==3:
		obs_pic=pygame.image.load("car4.png")
	if obs==4:
		obs_pic=pygame.image.load("car5.png")
	if obs==5:
		obs_pic=pygame.image.load("car6.png")

	gamedisplays.blit(obs_pic,(obs_start_x,obs_start_y))	
	
def car(x,y):
	gamedisplays.blit(carImg,(x,y))

def score_system (passed,score):
	font = pygame.font.Font("freesansbold.ttf",50)
	text = font.render("Passed: "+str(passed),True,black)
	score = font.render("Score: "+str(score),True,red)
	gamedisplays.blit(text,(0,50))
	gamedisplays.blit(score,(0,0))

def text_type(text,font,colour):
	textSurface = font.render(text,True,colour)
	return textSurface,textSurface.get_rect()
	
def message_display(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_type(text,font,black)
	text_rectangle.center =(x,y)
	gamedisplays.blit(text_surface,text_rectangle)

def message_display_I(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_type(text,font,white)
	text_rectangle.center =(x,y)
	gamedisplays.blit(text_surface,text_rectangle)

def message_display_II(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_type(text,font,green)
	text_rectangle.center =(x,y)
	gamedisplays.blit(text_surface,text_rectangle)

def message_display_III(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_type(text,font,yellow)
	text_rectangle.center =(x,y)
	gamedisplays.blit(text_surface,text_rectangle)
	
def crash(x,y):
	global points
	gamedisplays.blit(crash_img,(x,y))
	message_display_III("You Crashed",115,display_width/2,display_height/2)
	pygame.display.update()
	time.sleep(2)
	again()
	pygame.display.update()
	clock.tick(20)	
	points = 0
		
def gameloop():
	global pause
	global points
	road_x1 = 300
	road_x2 = 300
	road_left_x1 = 0
	road_left_x2 = 0
	road_right_x1 = 1300
	road_right_x2 = 1300
	road_y1 = 0
	road_y2 = -1000
	road_left_y1 = 0
	road_left_y2 = -1000
	road_right_y1 = 0
	road_right_y2 = -1000
	road_speed = 35
	road_speed_change = 0
	road_left_speed = 35
	road_left_speed_change = 0
	road_right_speed = 35
	road_right_speed_change = 0

	car_x = ((display_width / 2) - (car_width / 2))
	car_y = (display_height - car_height)
	car_x_change = 0

	road_start_x = 300
	road_end_x = 1300
	
	obs = 0
	obs_start_x = random.randrange(road_start_x,road_end_x-car_width)
	obs_start_y = -1000
	obs_width = 100
	obs_height = 200
	obs_speed = 10

	passed = 0
	level = 0
	score = 0
	gameExit = False
	
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and car_x > 300+obs_speed:
					car_x_change = -5
				elif event.key == pygame.K_RIGHT and car_x < (1300-car_width-obs_speed):
					car_x_change = 5
				elif event.key == pygame.K_a: 
					obs_speed += 2
				elif event.key == pygame.K_d:
					obs_speed -= 2
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					car_x_change = 0
			
		car_x+=car_x_change

		gamedisplays.blit(roadImg,(road_x1,road_y1))
		gamedisplays.blit(roadImg,(road_x2,road_y2))
		gamedisplays.blit(road_left,(road_left_x1,road_left_y1))
		gamedisplays.blit(road_left,(road_left_x2,road_left_y2))
		gamedisplays.blit(road_right,(road_right_x1,road_right_y1))
		gamedisplays.blit(road_right,(road_right_x2,road_right_y2))

		car(car_x,car_y)
		score_system(passed,score)
		obstacle(obs_start_x,obs_start_y,obs)
		obs_start_y += obs_speed

		if obs_start_y > display_height:
			obs_start_x = random.randrange(road_start_x,road_end_x-car_width)
			obs_start_y = -200
			obs = random.randrange(0,6)
			passed += 1
			score = passed*10
			points = score
			if int(passed)%10 == 0:
				
				level += 1
				obs_speed+3
				message_display("LEVEL"+str(level),100,display_width/2,display_height/2)
				pygame.display.update()
				time.sleep(2)

		road_y1 += road_speed
		road_y2 += road_speed
		
		if road_y1 >= display_height:
			road_y1 = -1000
			
		if road_y2 >= display_height:
			road_y2 = -1000

		road_left_y1 += road_left_speed
		road_left_y2 += road_left_speed
		
		if road_left_y1 >= display_height:
			road_left_y1 = -1000
			
		if road_left_y2 >= display_height:
			road_left_y2 = -1000

		road_right_y1 += road_right_speed
		road_right_y2 += road_right_speed
		
		if road_right_y1 >= display_height:
			road_right_y1 = -1000
			
		if road_right_y2 >= display_height:
			road_right_y2 = -1000


		if car_x > road_end_x-car_width:
			crash(car_x,car_y)
		if car_x < road_start_x:
			crash(car_x,car_y)

		if car_y < obs_start_y+obs_height:
			if car_x >= obs_start_x and car_x <= obs_start_x+obs_width:
				crash(car_x,car_y-50)
			if car_x+car_width >= obs_start_x and car_x+car_width <= obs_start_x+obs_width:
				crash(car_x,car_y-50)

		Buttons("Pause",1450,0,150,50,blue,yellow,"pause")
		pygame.display.update()
		clock.tick(60) 

introloop()		
gameloop()	
pygame.quit()
quit()
