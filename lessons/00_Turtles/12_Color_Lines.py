"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    ... # Your code here


# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here
tina.circle(100,steps= 30)
tina.forward(100)
tina.clone(2)                   # Close the window when we click on it
tina.hideturtle
tina.forward(20)
tina.left(60)
tina.clone
tina.