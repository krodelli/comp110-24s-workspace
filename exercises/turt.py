"""This is a house with windows and a smoking chimmney. Function for drawing the body of the house (a square) is located on lines 9-25. Roof funtion on lines 27-43. Windows (this is my draw something twice (3 times) function) on lines 45-65. Chimney is drawn with function lines 67-80. The recursive funtion is my smoke, which is on lines 82-100. The main function is at the end of my document, and is the last function. It calls all of my functions and sets the scene. For splitting up, I originally had the roof and square functions together, but it made more sense to split it up, that way i could color them different things as well. Lastly, I used xcor() on line 62 to move the turtle to a new position based on the x-coordinate, the size, and a multiplier of 1.5. """

__author__ = "730466512"


from turtle import Turtle, colormode, done


colormode(255)
class Turtle: 

    def draw_square(a_turtle: Turtle, x: float, y: float, width: float, fill: list[int]) -> None:
        """Draw a square of given width whose top left corner is at x,y."""
        a_turtle.penup()
        a_turtle.goto(x, y)  # Lower the square.
        a_turtle.setheading(0.0)  # Make sure turtle facing the right way.
        a_turtle.pendown()
        for elem in range(4):
            a_turtle.forward(width)
            a_turtle.right(90)
        for _ in range(4):
            a_turtle.begin_fill()
            a_turtle.fillcolor(fill)
            for _ in range(4):
                a_turtle.forward(width)
                a_turtle.right(90)
            a_turtle.end_fill()


    def draw_roof(a_turtle: Turtle, x: float, y: float, width: float, fill: list[int]) -> None:
        """Draw the roof for the house."""
        a_turtle.penup()
        a_turtle.goto(x, y)  
        a_turtle.setheading(60)
        a_turtle.pendown()
        for elem in range(3):
            a_turtle.forward(width)
            a_turtle.right(120)
        for elem in range(3):
            a_turtle.begin_fill()
            a_turtle.fillcolor(fill)
            for elem in range(3):
                a_turtle.forward(width)
                a_turtle.right(120)
            a_turtle.end_fill()


    def draw_windows(t: Turtle, x_start: float, y_start: float, size: float, num_windows: int, border_color: str, fill_color: list[int]) -> None:
        """Draw repeating square windows."""
        t.penup()
        t.goto(x_start, y_start)  # Lower the windows.
        t.setheading(0.0)
        t.pendown()
        t.color(border_color)

        for _ in range(num_windows):
            # Draw window frame.
            t.begin_fill()
            t.fillcolor(fill_color)
            for _ in range(num_windows):
                t.forward(size)
                t.right(90)
            t.end_fill()
            # Move to the next window position.
            t.penup()
            t.goto(t.xcor() + size * 1.5, y_start - size)
            t.pendown()


    def draw_chimney(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
        """Draw a chimney at the specified position and size."""
        turtle.penup()
        turtle.goto(x, y)  # Move to the starting position.
        turtle.pendown()
        turtle.fillcolor("brown")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(height)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
        turtle.end_fill()


    def draw_smoke(turtle: Turtle, x: float, y: float, size: float, depth: float) -> None:
        """Draw smoke above the chimney using recursion."""
        if depth == 0:
            return
        turtle.penup()
        turtle.goto(x, y)  # Move to the starting position.
        turtle.pendown()
        turtle.fillcolor("gray")
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        new_x = x + size * 0.7  #  Adjust x position for the next smoke.
        new_y = y + size * 0.5  #  Adjust y position for the next smoke.
        new_size = size * 0.8  #  Reduce size for the next smoke.
        draw_smoke(turtle, new_x, new_y, new_size, depth - 1)


    def main() -> None:
        """The entry point of my scene."""
        turtle = Turtle()
        turtle.speed(0)
        turtle.hideturtle()
        draw_square(turtle, -150.0, 100.0, 250.0, [180, 158, 154])
        draw_roof(turtle, -150.0, 100.0, 250.0, [105, 93, 93])
        window_size = 50.0  #  Adjust window size as needed.
        num_windows = 3
        draw_windows(turtle, -125.0, 80.0, window_size, num_windows, "brown", [173, 245, 241])
        chimney_width = 20.0
        chimney_height = 100.0
        chimney_x = -120.0
        chimney_y = 200.0
        draw_chimney(turtle, chimney_x, chimney_y, chimney_width, chimney_height)
        smoke_size = 30.0
        smoke_depth = 6.0
        smoke_x = chimney_x + 20
        smoke_y = chimney_y + 20
        draw_smoke(turtle, smoke_x, smoke_y, smoke_size, smoke_depth)
        done()


    if __name__ == "__main__":
        main()