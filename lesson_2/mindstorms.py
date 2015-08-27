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

def draw_triangle():
    jennifer = turtle.Turtle()
    jennifer.shape("classic")
    jennifer.color("black")

    for i in range(3):
        jennifer.forward(100)
        jennifer.left(120)

window = turtle.Screen()
window.bgcolor("red")

draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
