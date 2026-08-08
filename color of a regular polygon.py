import turtle


def draw_polygon():
    screen = turtle.Screen()
    screen.title("Regular Polygon Generator")

    try:

        side = int(screen.numinput("Input Required", "Enter the number of sides:", minval=3))
        length = float(screen.numinput("Input Required", "Enter the length of each side:", minval=1))
        line_color = screen.textinput("Input Required", "Enter the line color (e.g., 'black', 'blue'):")


        fill_color = screen.textinput("Input Required", "Enter the fill color (e.g., 'gold', 'red'):")
    except (TypeError, ValueError):
        print("Invalid input or operation cancelled.")
        return


    if not line_color: line_color = "black"
    if not fill_color: fill_color = "lightgray"

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)

    try:

        t.color(line_color, fill_color)
    except turtle.TurtleGraphicsError:
        print("Invalid color name entered. Defaulting to black and gray.")
        t.color("black", "lightgray")


    angle = 360 / side


    t.begin_fill()
    for _ in range(side):
        t.forward(length)
        t.right(angle)
    t.end_fill()

    t.hideturtle()
    screen.exitonclick()



if __name__ == "__main__":
    draw_polygon()
