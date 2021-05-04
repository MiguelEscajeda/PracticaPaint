from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    "Draw circle from start to end."
    begin_fill()
    circle(end.x-start.x)  # TODO
    end_fill()

def rectangle(start, end):
   "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        if count== 0 or count==2:
            forward(end.x - start.x)
            left(90)
            print(count)
        else:
            forward(end.x + start.x)
            left(90)
            print(count)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        #saca, extrae el valor que tiene la var state en la llave 'shape'
        shape = state['shape']
        
        #Crea un objeto de tipo vector con x,y y lo guarda en el end
        end = vector(x, y)
        
        #el contenido de shape indica la funcion que se ejecutara
        shape(start, end)
        
        #reinicializar start con none-indicar que lo siguiente es nuevo
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
#Funcion que sirve para crear una ventana de ancho 420, alto 420
#los ultimos dos argumentos indican- la posicion de la esquina superior izquiera
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('#F1C40F'), 'Y')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
