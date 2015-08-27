import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(4):
        brad.forward(100)
        brad.right(90)
    

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")

    angie.circle(100)



window = turtle.Screen()
window.bgcolor("red")

draw_square()
draw_circle()

window.exitonclick()
