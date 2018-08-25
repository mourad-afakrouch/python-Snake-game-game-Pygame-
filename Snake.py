import random
import pygame, sys
from pygame.locals import *
from time import sleep
pygame.init()
font = pygame.font.Font(None, 36)
game_over= False
#Game Name
pygame.display.set_caption("My Snake Game")
# define Colors
GREEN = (20, 200, 255)
BLACK = (0, 60,0)
WHITE = (255, 255, 255)
snake_width = 20
direction = 'right'
x_step = 1
y_step = 0
class Point:
    def __init__(self, x, y):
        self.snake_x = x
        self.snake_y = y
    snake_x = 100
    snake_y = 100
makla = Point(200, 200)
lpoint = []
mypoint1 = Point(100, 100)
mypoint2 = Point(100 + snake_width, 100)
mypoint3 = Point(100 + (2 * snake_width), 100)
mypoint4 = Point(100 + (3 * snake_width), 100)
mypoint5 = Point(100 + (4 * snake_width), 100)
lpoint.append(mypoint1)
lpoint.append(mypoint2)
lpoint.append(mypoint3)
lpoint.append(mypoint4)
lpoint.append(mypoint5)
def computeDirection(direct):
    global x_step
    global y_step
    if direct == "right":
        x_step = 1
        y_step = 0
    if direct == "left":
        x_step = -1
        y_step = 0
    if direct == "up":
        x_step = 0
        y_step = -1
    if direct == "down":
        x_step = 0
        y_step = 1
# set up pygame
pygame.init()
# set up the window
windowSurface = pygame.display.set_mode((800, 600), 0, 32)
# draw the white background onto the surface
windowSurface.fill(GREEN)
# draw the window onto the screen
pygame.display.update()
# define drawing shapes
def putPixel(x, y):
    windowSurface.set_at((x, y), BLACK)
def Hline(x1, y1, x2, y2):
    for i in range(x2 - x1):
        putPixel(x1 + i, y1)
def Vline(x1, y1, x2, y2):
    for i in range(y2 - y1):
        putPixel(x1, y1 + i)
def rectangle(x, y):
    Hline(x, y, x + snake_width, y)
    Hline(x, y + snake_width, x + snake_width, y)
    Vline(x, y, x, y + snake_width)
    Vline(x + snake_width, y, x + snake_width, y + snake_width)
def updateSnake(lp):
    for k, v in enumerate(lp):
        if (k < len(lp)-1):
            lp[k].snake_x = lp[k + 1].snake_x
            lp[k].snake_y = lp[k + 1].snake_y
        else:
            lp[k].snake_x = lp[k].snake_x + (snake_width * x_step)
            lp[k].snake_y = lp[k].snake_y + (snake_width * y_step)
def draw_snake(snake_list):
    for mypoint in snake_list:
        rectangle(mypoint.snake_x, mypoint.snake_y)
def snake_zone():
    global mypoint5
    if  mypoint5.snake_x == -20 :
         mypoint5.snake_x = 800
    elif mypoint5.snake_x == 820 :
         mypoint5.snake_x = 0
    elif mypoint5.snake_y == -20 :
         mypoint5.snake_y = 600
    elif  mypoint5.snake_y == 620:
         mypoint5.snake_y=0
# makla
list1 = []
list2 = []
def random_list():
    rx = 0
    while rx < 720:
        rx += 20
        list1.append(rx)
    ry = 0
    while ry < 520:
        ry += 20
        list2.append(ry)
random_list()
def randmakla():
    global makla
    makla = Point(random.choice(list1), random.choice(list2))
randmakla()
def drawmakla():
    rectangle(makla.snake_x, makla.snake_y)
def CheckOukla():
    global makla
    if makla.snake_x == mypoint5.snake_x and makla.snake_y == mypoint5.snake_y:
        lpoint.insert(0,makla)
        randmakla()
#game over
def over(listsnake):
    global game_over
    lsnake1=listsnake[:-1]
    for cube in lsnake1:
        if listsnake[-1].snake_x == cube.snake_x:
            if listsnake[-1].snake_y == cube.snake_y:
                game_over=True



# run the game loop
while True:
    windowSurface.fill(GREEN)
    draw_snake(lpoint)
    drawmakla()
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if mypoint5.snake_x > mypoint4.snake_x:
            direction = 'right'
        else:
            direction= 'left'
    if keys[K_RIGHT]:
        if mypoint5.snake_x < mypoint4.snake_x:
            direction = 'left'
        else:
            direction= 'right'
    if keys[K_UP]:
        if mypoint5.snake_y > mypoint4.snake_y:
            direction = 'down'
        else:
            direction= 'up'
    if keys[K_DOWN]:

        if mypoint5.snake_y < mypoint4.snake_y:
            direction = 'up'
        else:
            direction= 'down'

    sleep(0.07)
    computeDirection(direction)
    updateSnake(lpoint)
    over(lpoint)
    if game_over:
        windowSurface.fill(BLACK)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = windowSurface.get_width() / 2 - text_rect.width / 2
        text_y = windowSurface.get_height() / 2 - text_rect.height / 2
        windowSurface.blit(text, [text_x, text_y])
    snake_zone()
    CheckOukla()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
