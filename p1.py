import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest drawing speed

# Function to draw a colorful spiral
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
    
    for i in range(360):
        spiral_turtle.pencolor(colors[i % len(colors)])  # Change color
        spiral_turtle.width(i / 100 + 1)  # Change width
        spiral_turtle.forward(i)  # Move forward
        spiral_turtle.right(59)  # Turn right

# Call the function to draw the spiral
draw_spiral()

# Hide the turtle and finish
spiral_turtle.hideturtle()
turtle.done()