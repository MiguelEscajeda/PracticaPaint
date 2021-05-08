# Miguel Angel Escajeda Anaya
# A00829399
# 07/Mayo/2021
# En este curso tuve la oportunidad de ver mas a fondo la implementacion de la libreria freegames y turtle para
# el desarrollo de videojuegos, ademas de permitirme retomar el lenguaje de python y ampliar mi conocimiento en
# este, tambien fue una oportunidad para desarrollar mi pensamiento logico para la solucion de prblemas y retos
# como los presentados en las actividades de este curso en las que se tuvo que pensar de forma creativa e
# investigar para encontrar soluciones a estos retos, dentro del aprendizaje tambein se encuentra el desarrollo
# del trabajo colaborativo que en esta ocasion fue en plenaria lo que pude ser mas enriquecedor ya que se
# compartiand ideas de solucion a los retos que eran muy creativas y que por mimismo tal vez no encontaria
# pero al ver como esta idea podia solucionar la problematica me dio un campo de vision mas amplia para enfrentarme
# a futuros retos o situaciones problemas y encontrar su solucion de manera mas creativa y sencilla, como ultimo
# todo este curso me permitio ver que el desarrollo de videojuegos no esta tan lejos de nosotros y que incluso no
# siendo experto podemos trabajar en juegos clasicos y desarrollarlos lo que me lleva a querer aprender mas sobre
# ambito y querer seguir aprendiendo sobre el desarrollo de videojuegos.

# Link video: https://youtu.be/1Bh7eB99CkE
# Link Github: https://github.com/MiguelEscajeda/Practicas.git

from random import *
from turtle import *
from freegames import path

# Regresa el full path to 'filname' in freegames module

# Llama a la imagen modificada

car = path('car2.gif')

# Indica la baraja que sera utilizada

tiles = ['Pera','Manzana','Mango','Fresa','Kiwi','Sandia','Melon','Durazno','Aguacate','Zanahoria','Granada','Calabaza','Berenjena','Papaya','Naranja','Toronja',
         'Mandarina','Uva','Mora','Cereza','Cebolla','Brocoli','Rabano','Arandano','Frambuesa',
         'Guayaba', 'Limon','Piña','Platano','Coco','Ciruela','Higo'] * 2
state = {'mark': None}
hide = [True] * 64
taps = 0
writer=Turtle(visible=False)

# Funcion encargada de dibujar los cuadrados del tablero

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'blue')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Convierte las coordenadas del click en numero de tarjeta
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
# Convierte las tarjetas en sus posiciones x,y
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# funcion callback cuando das clic sobre la ventana
def tap(x, y):
    global mark, taps
    
    # Imprime las coordenadas donde se dio link
    print(x,y)
    
    taps = taps + 1
    "Update mark and hidden tiles based on tap."
    # retorna el indice correspondiente a (x,y) en tiles[spot]
    spot = index(x, y)
    
    # saca el valor de state- al inicio es None
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # el estado ahora cambia a la carta donde el usuario dio click
        state['mark'] = spot
    else:
        #quiere decir que son pares y las hace visibles
        hide[spot] = False
        hide[mark] = False
        # vuelve a mark none que no tenmos una carta visible
        state['mark'] = None

def draw():
    "Draw image and tiles."
    # Limpia la ventana
    clear()
    # mueve el turtle a la posicion 0,0
    goto(0, 0)
    # carga la imagen del auto
    shape(car)
    # dibuja el auto centrado, el centro de la imagen se pone en la coordenadas
    # donde este turtle
    stamp()
    
    # Dibuja las 64 cartas del memorama
    # Inicialmente todas las cartas estan escndidas
    contador=0
    for count in range(64):
        # si todavia no esta descubierta la carta su valor sera true
        if hide[count]:
            # Calcula su equivalencia en el tablero
            x, y = xy(count)
            # dibuja un square en la posicion x,y
            square(x, y)
            # dibuja el numero de la casillas
            #write(f'{count', font=('Arial',30,'normal'))
            # cuenta la cantidad de cartas escondidas
            contador= contador + 1
        # que pasa si hide[count]== Flase no lo dibuja
    # None significa que  no hay carta visible
    # ### index de la carta visible
    mark = state['mark']

    # Si el estado no es None y esa carta no esta descubierta
    if mark is not None and hide[mark]:
        # calcula la posicion x. y de la carta
        x, y = xy(mark)
        # levanta el lapiz
        up()
        # mueve el turtle a la posicion de x+2
        goto(x + 1, y)
        # cambia el color del lapiz
        color('black')
        # despliega en esa posicion x + 2 y el numero de la carta oculfta
        write(tiles[mark], font=('Arial', 13, 'normal'))
    
    #Verifica si ya logro encontrar todos los pares
    escondidas=hide.count(True)
    print("Sin encontrar hide.count(True)=", escondidas)
    print(" Sin encontrar contador=", contador)
    if escondidas==0:
        up()
        goto(-100,0)
        color("white")
        write("Ganaste", font=('Arial',30,'normal'))
        goto(-50,-25)
        write(f'Hiciste {taps} taps')
        nombres()
        return
    
    # muestra en la ventana lo dibujado
    update()
    # vuelve a llamar a la funcion draw() en 10 seg
    ontimer(draw, 100)
    
def nombres():
    writer.up()
    writer.goto(-180,150)
    writer.color('black')
    writer.write('Miguel Angel Escajeda Anaya', font=('Arial',20,'normal'))
    

# Revolver la baraja de la memorama - tiles
shuffle(tiles)
setup(420, 420, 0, 0)
addshape(car)
hideturtle()
tracer(False)
#Detectar eventos del mouse
onscreenclick(tap)
nombres()
draw()
done()