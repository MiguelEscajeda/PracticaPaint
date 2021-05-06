import random
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
posf = [vector(-10,0), vector(10,0), vector(0,-10),vector(0,10)]
cs=0
colores = ['green','blue','yellow','pink','darkviolet']
color = "black"
color2 = "green"

def selectcolor():
    global color
    color = random.choice(colores)
    return color

def selectcolor2():
    global color
    global color2
    color2 = random.choice(colores)
    while color == color2:
        color2 = random.choice(colores)
    return color2

#Nos indica cel cambio de direccion de la serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    
#determina si la serpiente se encuentra dentro de los bordes
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Determina el movimiento de la serpiente
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
#Nos dice si pierde la serpiente    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
#se encarga de mover la comida cuando es alcanzada por la serpiente y moverla aleatoriamente mientras no es comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        selectcolor()
        selectcolor2()
    else:
        snake.pop(0)
        
#Si la comida no es atrapada es movida aleatoriamente y si se sale de la ventana regresa al origen    
    if head != food:
        food.move(random.choice(posf))
        if inside(food)==False:
            write("la food salio de la ventana")
            food.x=0
            food.y=0

    clear()

#Se encarga de hacer el cuerpo de la serpiente    
    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
