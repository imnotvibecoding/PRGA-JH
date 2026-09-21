import math
import turtle

amplituda = 150     # v pixelech
frekvence = 1.0     # kolik kmitů za "jednotku času" — zkus 2, 0.5
tlumeni = 0.3       # zkus 0.3

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# osa času
t.penup(); t.goto(-350, 0); t.pendown(); t.goto(350, 0)
t.penup(); t.goto(-350, 0); t.pendown()

t.pencolor("pink")
t.pensize(12)
for i in range(700):
    cas = i / 100
    y = amplituda * math.sin(2 * math.pi * frekvence * cas) * math.exp(-tlumeni * cas)
    t.goto(-350 + i, y)

turtle.done()