#-----import statements-----
import turtle as trtl

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second


#-----initialize turtle-----
counter =  trtl.Turtle()
score = trtl.Turtle()
target = trtl.Turtle()

#-----game functions-----
counter.penup()
counter.hideturtle()
counter.goto(330,350)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    game_over()
  else:
    counter.write("Timer: " + str(timer), align="center", font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def score():
    score.write("Score: " + str(score), align="center", font=font_setup)
    score.clear()
def game_over()
    target.ht()

#---------events---------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()

