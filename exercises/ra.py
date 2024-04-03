from turtle import Turtle

def draw_windows(t: Turtle, x_start: int, y_start: int, size: int, num_windows: int, border_color: str) -> None:
    """Draw repeating square windows."""
    t.penup()
    t.goto(x_start, y_start)  # Lower the windows
    t.setheading(0.0)
    t.pendown()
    t.color(border_color)

    for _ in range(num_windows):
        # Draw window frame
        for _ in range(4):
            t.forward(size)
            t.right(90)

        # Move to the next window position
        t.penup()
        t.goto(t.xcor() + size * 1.5, y_start - size)
        t.pendown()

def color_windows(t: Turtle, x_start: int, y_start: int, size: int, num_windows: int, fill_color: str) -> None:
    """Color all windows with the specified color."""
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    t.begin_fill()
    t.fillcolor(fill_color)

    for _ in range(num_windows):
        for _ in range(4):
            t.forward(size)
            t.right(90)

        t.penup()
        t.goto(t.xcor() + size * 1.5, y_start - size)
        t.pendown()

    t.end_fill()

def main():
    t = Turtle()
    t.speed(0)  # Set the drawing speed (0 is fastest)
    draw_windows(t, -100, 0, 50, 3, "black")
    color_windows(t, -100, 0, 50, 3, "lightblue")
    t.hideturtle()
    t.done()
