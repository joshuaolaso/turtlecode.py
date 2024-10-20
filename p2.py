import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)  # Fastest drawing speed

# Function to draw a flower petal
def draw_petal(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw a flower
def draw_flower(turtle, num_petals, radius, color):
    angle = 360 / num_petals
    for _ in range(num_petals):
        draw_petal(turtle, radius, color)
        turtle.right(angle)

# Function to draw a garden of flowers
def draw_garden(turtle, num_flowers, num_petals, radius):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta", "khaki", "pink", "grey", "skyblue", "darkgreen", "yellowgreen"]
    for _ in range(num_flowers):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.penup()
        turtle.screenfill("imiss you")
        turtle.goto(x, y)
        turtle.pendown()
        draw_flower(turtle, num_petals, radius, random.choice(colors))

# Call the function to draw the garden
draw_garden(flower_turtle, 10, 10, 20)

# Hide the turtle and finish
flower_turtle.hideturtle()
turtle.done()