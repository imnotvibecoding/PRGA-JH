import math
import time
import turtle

delka = 400       # délka závěsu v pixelech
uhel_max = 0.6      # největší výchylka v radiánech (0.6 ≈ 34°)
tlumeni = 0.1       # 0 = houpe se napořád
snimku_za_s = 60    # rychlost animace

okno = turtle.Screen()
okno.tracer(0)                      # kreslíme sami, ať to neblikne
k = turtle.Turtle()
k.hideturtle()

for i in range(600):
    cas = i / 30
    uhel = uhel_max * math.cos(2 * cas) * math.exp(-tlumeni * cas)
    x = delka * math.sin(uhel)
    y = 200 - delka * math.cos(uhel)
    k.clear()
    k.penup(); k.goto(0, 200); k.pendown(); k.goto(x, y)   # provázek
    k.dot(30, "firebrick")                                  # kulička
    okno.update()
    time.sleep(1 / snimku_za_s)          # bez pauzy proběhne vše naráz a vidíš jen poslední snímek

turtle.done()
