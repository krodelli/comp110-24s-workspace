"""House with repeating windows."""

__author__ = "730466512"

from turtle import Turtle, colormode, done
colormode(255)

def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of given width whose top left corner is at x,y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)  # make sure turtle facing right way.
    a_turtle.pendown()
    for elem in range(4):
        a_turtle.forward(width)
        a_turtle.right(90)

def draw_roof(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the roof for the house."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(60)
    a_turtle.pendown()
    for elem in range(3):
        a_turtle.forward(width)
        a_turtle.right(120)

def draw_windows(t: Turtle, x_start: int, y_start: int, size: int, num_windows: int, border_color: str, fill_color: str) -> None:
    """Draw repeating square windows."""
    t.penup()
    t.goto(x_start, y_start)
    t.setheading(0.0)
    t.pendown()
    t.color(border_color)

    for _ in range(num_windows):
        # Draw window frame
        t.begin_fill()
        t.fillcolor(fill_color)
        for _ in range(4):
            t.forward(size * 1.5)
            t.right(90)
        t.end_fill()

        # Draw window lines
        t.penup()
        t.goto(t.xcor() + size * 0.25, t.ycor())
        t.pendown()
        t.forward(size * 0.5)
        t.penup()
        t.goto(t.xcor() - size * 0.25, t.ycor() - size * 0.25)
        t.pendown()
        t.forward(size * 0.5)
        t.penup()

        # Move to the next window position
        t.goto(t.xcor() + size * 2.5, y_start)  # Adjust spacing between windows as needed
        t.pendown()

def main() -> None:
    """The entry point of my scene."""
    turtle = Turtle()
    turtle.speed(0)
    turtle.hideturtle()

    draw_square(turtle, -150.0, 150.0, 250.0)

    draw_roof(turtle, -150.0, 150.0, 250)

    window_size = 20  # Adjust window size as needed
    window_spacing = 50  # Adjust spacing between windows as needed
    num_windows = 4
    draw_windows(turtle, -100.0, 100.0, window_size, num_windows, "brown", "blue")
    done()

if __name__ == "__main__":
    main()