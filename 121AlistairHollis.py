#-----import statements-----
import turtle as trtl
import random
#-----game configuration-----
font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
size = 3
score = 1
speed = 0
wn = trtl.Screen()

#-----initialize turtle-----
counter =  trtl.Turtle()
scoreman = trtl.Turtle()
target = trtl.Turtle()
scoreman.ht()
scoreman.pu()
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
    target.goto(9001,9001)
    while True:
      wn.bgcolor("red")
      wn.bgcolor("orange")
      wn.bgcolor("yellow")
      wn.bgcolor("green")
      wn.bgcolor("blue")
      wn.bgcolor("indigo")
      wn.bgcolor("violet")

def target_move():

  randx = random.randint(-400,400)
  randy = random.randint(-300,300)

  target.goto(randx, randy)




#---------events---------
target.onclick(target_clicked)

wn.ontimer(countdown, counter_interval)
wn.mainloop()

