# O módulo turtle permite visualizar linhas a serem criadas e visualizar melhor a recursão.

# Neste caso vai-se criar uma Turtle e criar uma função para desenhar uma espiral:

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        drawSpiral(myTurtle, lineLen-2)

drawSpiral(myTurtle, 100)
myWin.exitonclick()
