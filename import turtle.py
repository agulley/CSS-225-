import turtle
import colorsys
def draw_creative_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Creative Turtle Mandala")
    t= turtle.Turtle()
    t.speed(0)
    t.width(2)
    turtle.delay(0)
    total_line =210
    hue =0.0
    for i in range(total_line):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(color)
        hue += 1.0 / total_line
        if i % 30 == 0:
            t.width(t.width() + 1)
        elif i % 45 == 0:
            t.width(max(1, t.width() - 1))
        t.forward(i * 2)
        t.left(144)
        t.forward(i)
        t.right(45)
        if i % 15 == 0:
            t.dot(i // 10, "white")
            t.hideturtle()
            screen.mainloop()
        if_name_= "_main_"
        draw_creative_spiral()