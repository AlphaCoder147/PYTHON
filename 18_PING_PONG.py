import turtle
import winsound
#Window Initialisation
window=turtle.Screen()
window.title("Pong by Advait Keskar")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.penup()
paddle_a.shapesize(stretch_len=1,stretch_wid=6)
paddle_a.goto(-350,0)

# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.penup()
paddle_b.shapesize(stretch_len=1,stretch_wid=6)
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0,0)
ball.dx=0.04
ball.dy=-0.04

#Score
score=turtle.Turtle()
score.speed(0)
score.color("White")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: 0  Player B: 0",align="center",font=("Arial",25,"bold"))
pt_a=0
pt_b=0

# Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
 
# Key Bindings
window.listen()
window.onkeypress(paddle_a_up,"w")       
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")            
window.onkeypress(paddle_b_down,"Down")
#Game LOOP
while True:
    window.update()
# Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
# Border Check
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*= -1
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*= -1
        pt_a+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(str(pt_a),str(pt_b)),align="center",font=("Arial",25,"bold"))
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        pt_b+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(str(pt_a),str(pt_b)),align="center",font=("Arial",25,"bold"))
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)
# Ball and Paddle collisions
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)
    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1                              
        winsound.PlaySound("bounce_ping.wav",winsound.SND_ASYNC)