import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake Game - by Dany Mastandrea")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup() #quita el rastro al moverlo
cabeza.goto(0,0) #comienza en el centro
cabeza.direction = "stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("green")
comida.penup() 
comida.goto(0,120) 

#Segmentos / cuerpo serpiente

segmentos = []

# crear texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup() #no se ve lapluma
texto.hideturtle() #escondela pluma
texto.goto(0,260) #centrado arriba
texto.write("Score: 0       High Score: 0", align="center", font=("Courier", 24,"normal" ))



#Funciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"            

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)        

#teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    #Choque con los bordes
    if cabeza.xcor() >280 or cabeza.xcor() <-280 or cabeza.ycor() >280 or cabeza.ycor() <-280:
        time.sleep(1)
        cabeza.goto (0,0)
        cabeza.direction = "stop"

        # Esconder segmentos

        for segmento in segmentos:
            segmento.goto(2000,2000)

        # limpiar lista de segmentos
        segmentos.clear() 

        #Reset marcador
        score = 0
        texto.clear()
        texto.write(f"Score: {score}       High Score: {high_score}", align="center", font=("Courier", 24,"normal" ))  


    #comer
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto (x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup() 
        segmentos.append(nuevo_segmento)
        
        #aumentar score
        score +=10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write(f"Score: {score}       High Score: {high_score}", align="center", font=("Courier", 24,"normal" ))    

    # mover el cuerpo
    totalSeg = len(segmentos)
    for index in range (totalSeg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov ()

    #colision cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) <20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            #esconde segmentos
            for segmento in segmentos:
                segmento.goto(1500,1500)

            segmentos.clear()

            score = 0
            texto.clear()
            texto.write(f"Score: {score}       High Score: {high_score}", align="center", font=("Courier", 24,"normal" ))    

    time.sleep (posponer)




