"""
from turtle import *
from random import random
from freegames import line

def draw():
    "Draw maze."
    color('black')
    width(5)

    for x in range(-200,200,40):
        for y in range(-200,200,40):
            if random() > 0.5:
                line(x,y,x+40,y+40)
            else:
                line(x,y+40,x+40,y)
    update()

def tap(x,y):
    "Draw line and dot for screen tap"
    if abs(x)>198 or abs(y)>198 :
        up()
    else:
        down()
    width(2)
    color('red')
    goto(x,y)
    dot(4)

setup(420,420,370,0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
"""
import turtle
import math
#background and UI
wn = turtle.Screen()
wn.bgcolor('#ffd26c')
wn.title('Desert Temple Maze')
wn.setup(700, 700)
wn.tracer(0)
 
#maze walLs
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('#ff7227')
        self.penup()
        self.speed(0)
#player model
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color('#fe5d5d')
        self.penup()
        self.speed(0)
        self.gems = 0
         
    #movement of player   
    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor() + 24
         
        #so player detects the walls
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
   
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor() - 24
     
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)  
         
    def go_right(self):
        move_to_x=player.xcor() + 24
        move_to_y=player.ycor()
     
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y) 
         
    def go_left(self):
        move_to_x=player.xcor() - 24
        move_to_y=player.ycor()
     
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    #detects items near player
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
 
        if distance < 5:
            return True
        else:
            return False 
#create treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color('light green')
        self.penup()
        self.speed(0)
        self.gems = 100
        self.goto(x,y)
 
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
 
         
levels = [""]
""" 
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XPX         X           X",
"X X XXXXX XXXXXX XXXXXX X",
"X X    TX        X      X",
"X XXXXXXX XXXXXXXXXXXXX X",
"X         X  TX X     X X",
"XXXXX XXXXX XXX X XXXXX X",
"X   X X     X X         X",
"X X X   XXXXX X XXXXXXXXX",
"X X XXXXX               X",
"X X       XXXXXXXXX XXX X",
"X XXXXXX XX       X XTX X",
"X      X  X XXXXX X X X X",
"XXXXXX XX X     X X X X X",
"X       XTX XX XXXX X X X",
"X XXXXXXXXX X     X X   X",
"X X     X   XXXXX X XXXXX",
"X XXX X X X X  TX X    TX",
"X     X X X X XXX XXXXXXX",   
"XXXXX X   X X   X X     X",
"X   X XXXXXXXXX X   XXX X",
"X XTX X       X XXXXX   X",
"X XXX XXXXX X X   XTX   X",
"X           X   X   X   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
"""
level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XPX XXX                 X",
"X X XXX   XXXXXX XXXXXX X",
"X X    TX        X      X",
"X XXXXXXX XXXXXXXXXXXXX X",
"X         X  TX X     X X",
"XXXXX XXXXX XXX X XXXXX X",
"X   X X     X X         X",
"X X X   XXXXX X XXXXXXXXX",
"X X XXXXX               X",
"X X       XXXXXXXXX XXX X",
"X XXXXXX XX       X XTX X",
"X      X  X XXXXX X X X X",
"XXXXXX XX X     X X X X X",
"X       XTX XX XXXX X X X",
"X XXXXXXXXX X     X X   X",
"X X     X   XXXXX X XXXXX",
"X XXX X X X X  TX X    TX",
"X     X X X X XXX XXXXXXX",   
"XXXXX X   X X   X X     X",
"X   X XXXXXXXXX X   XXX X",
"X XTX X       X XXXXX   X",
"X XXX XXXXX X X   XTX   X",
"X           X   X   X   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
 
#creates treasure list
treasures = []
 
#Add maze to mazes list
#levels.append(level_1)
levels.append(level_2)
#Level Setup
 
def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      character = level[y][x]
      #Calculate the screen x, y coordinates
      screen_x = -288 + (x * 24)
      screen_y = 288 - (y * 24)
       
      #Check if it is an X
      if character == "X":
        pen.goto(screen_x, screen_y)
        pen.stamp()
        walls.append((screen_x,screen_y))
 
      #representing player on maze  
      if character == "P":
        player.goto(screen_x, screen_y)
 
      #representing treasure on maze
      if character == 'T':
          treasures.append(Treasure(screen_x, screen_y))
         
 
#variables
pen = Pen()
player = Player()
 
#creates list for wall coordinates
walls = []
 
#sets up level
setup_maze(levels[1])
print(walls)
   
#so the code responds to key presses
turtle.listen()
turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")
 
#turn off screen updates
wn.tracer(0)
 
#game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gems += treasure.gems
            print('Player gems: {}'.format(player.gems))
            treasure.destroy()
            treasures.remove(treasure)
    #update screen
    wn.update()