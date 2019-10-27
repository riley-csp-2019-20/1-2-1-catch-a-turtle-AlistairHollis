#-----import statements-----
import turtle as trtl
import random
import time
#-----game configuration-----
font_setup = ("impact", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
size = 3
figure = "circle"
score = 0
speed = 0
wn = trtl.Screen()

#-----initialize turtle-----
target = trtl.Turtle()
target.shape(figure)
counter =  trtl.Turtle()
scoreman = trtl.Turtle()
scoreman.hideturtle()
scoreman.penup()
target.pu()
target.speed(speed)
scoreman.goto(-360,350)
target.shapesize(size)

#-----game functions-----


counter.penup()
counter.hideturtle()
counter.goto(330,350)
def target_clicked(x,y):
  score_change()
  target_move()
def countdown():
  global timer
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    game_over()
  else:
    counter.write("Timer: " + str(timer), align="center", font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def score_change():
    global score
    score += 1
    scoreman.clear()
    scoreman.write("Score: " + str(score), align="center", font=font_setup)
def game_over():
    target.ht()
    counter.clear()
    target.goto(9001,9001)
    counter.goto(0,0)
    font_setup = ("impact", 70, "normal")
    counter.write("Time's Up", font=font_setup)
    while True:
      wn.bgcolor("red")
      time.sleep(0.2)
      wn.bgcolor("orange")
      time.sleep(0.2)
      wn.bgcolor("yellow")
      time.sleep(0.2)
      wn.bgcolor("green")
      time.sleep(0.2)
      wn.bgcolor("blue")
      time.sleep(0.2)
      wn.bgcolor("indigo")
      time.sleep(0.2)
      wn.bgcolor("purple")
      time.sleep(0.2)

def target_move():

  randx = random.randint(-400,400)
  randy = random.randint(-300,300)

  target.goto(randx, randy)

#---------events---------
target.onclick(target_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()