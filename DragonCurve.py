import turtle

# Fungsi untuk menghasilkan Dragon Curve
def dragon_curve(t, order, size, sign=1):
    if order == 0:
        t.forward(size)
    else:
        t.right(45 * sign)
        dragon_curve(t, order - 1, size / 1.414, 1)
        t.left(90 * sign)
        dragon_curve(t, order - 1, size / 1.414, -1)
        t.right(45 * sign)

# Set up turtle environment
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()

# Menggambar Dragon Curve
dragon_curve(t, 10, 400)

# Tunggu hingga jendela ditutup
turtle.done()
