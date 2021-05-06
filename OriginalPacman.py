#Miguel Anhel Escajeda Anaya
#A00829399
# Ernesto Flores 
# A00828975
# Reflexion
# 06-Mayo-2021

# Imports de todas las librerias al inicio
from random import choice
from turtle import *
from freegames import floor, vector

# Almacena el score-cantidad de bolitas comidas por pacman
state = {'score': 0}

# Hace invisible la turtle-- creando dos objetos de clase turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)
info = Turtle(visible=False)
tab = Turtle(visible=False)

# Direccion del Pacman
aim = vector(5, 0)

# Crea pacman en la posicion (-40,-80)
pacman = vector(-40, -80)

# Lista de listas de la posicion y direccion de cada fantasma
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    
    [vector(-180, -160), vector(0, 5)],
    
    [vector(100, 160), vector(0, -5)],
    
    [vector(100, -160), vector(-5, 0)],
]

# Lista de tablero para simular 20 columas x 20 renglones
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Dibuja un square con su esquina inferior izquierda en (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# retornar true si point es un tile valido
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)
    
    # Si la celda es 0 return false- pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    # Si la celda es 0 return false- pared
    if tiles[index] == 0:
        return False

    # return true?
    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    "Draw world using path."
    bgcolor('black')
    path.color('purple1')
    
    # Recorre toda la lista (tiles)
    for index in range(len(tiles)):
        tile = tiles[index]
    
    # Si el valor es 1
        if tile > 0:
            # Calcula x, y donde se dibuja el square
            x = (index % 20) * 20 - 200 
            y = 180 - (index // 20) * 20
            square(x, y)
            
            # Dinuja la bolita en el centro sobre el square de size 20
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(4, 'white')

def move():
    #muestra nuestro nombres
    def info_alumno1():
        info.up()
        info.goto(0,190)
        info.color('blue')
        info.write('ErnestoFloresA00828975', align='left', font=('Arial',12,'normal'))
        info.up()
        info.goto(-200,190)
        info.color('white')
        info.write('MiguelEscajedaA008293', align='left', font=('Arial',12,'normal'))
    info_alumno1()
    # Lista de colores paraz los fantasmas
    colores = ['red', 'green', 'pink', 'white']
    "Move pacman and all ghosts."
    
    # muestra el score
    tab.undo()
    tab.goto(150,150)
    tab.color('white')
    valor = state['score']
    tab.write(f'Score:{valor}')

    # Limpia la ventana
    clear()
    
    # Si es una posicion valida -no es pared- pacman.move(aim)
    if valid(pacman + aim):
        pacman.move(aim)
    
    # retorna la posicion del pacman e el tablero
    index = offset(pacman)

    # 1 - camino
    if tiles[index] == 1:
        # a esa posicion le asigna 2- comer la galleta
        tiles[index] = 2
        # se incrementa el score
        state['score'] += 1
        #calcula la posicion x,y del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        # dibujar el square - sin bolita
        square(x, y)

    up()
    # se va a la posicion del pacman
    goto(pacman.x + 10, pacman.y + 10)
    # 1era vez que se dibuja el pacman
    dot(20, 'yellow')

    k=0
    for point, course in ghosts:
        # Valida si el fantasma se puede mover en course
        if valid(point + course):
            point.move(course)
        else: # Si el fantasma no se puede mover en esa direccion
            # se actualiza a direccion del movimiento del mismo
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            # plan guarda nueva direccion del fantasm
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
            
            
        
        # levanta el lapiz
        up()
        # mueve a la posicion del fantasma
        goto(point.x + 10, point.y + 10)
        # Dibuja el fantasma
        dot(20, colores[k])
        # actualizar la posicion del fantasma
        k=k+1

    update()

    # recorre la lista de fantasma para ver si coinciden las
    # posiciones del pacman y de algun fantasma 
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-140,5)
            writer.write('GAME OVER', font=('Arial',30,'normal'))
            return
    # vuelve a llmar  a la funcion dentro e 100 milisegundos
    ontimer(move, 20)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Inicializa la ventana ancho 420, alto 420 y
# 370,0 indica la posicion de la esquina superior izquierda de la ventana en mi
# pantalla
setup(420, 420, 0, 0)

# Esconde la tortuga
hideturtle()

# Oculta toda forma de dibujar
tracer(False)

# Activar, escuchar los eventos del teclado
listen()

# En caso de que el usuario oprima la tecla indicada llama a la funcion change
# con los argumentos indicados que indican la nueva direccion del pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
# Llama a la funcion world-dibuja el tablero
world()
#Lllama la funcion move()
move()
# Hace un loop infinito qpara atender todos los eventos
done()
