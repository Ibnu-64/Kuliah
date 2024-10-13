import turtle

# Fungsi rekursif untuk menggambar sisi Koch
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

# Fungsi untuk menggambar Koch Snowflake
def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

# Set up turtle environment
t = turtle.Turtle()
t.speed(0)  # Kecepatan maksimum
screen = turtle.Screen()

# Menggambar snowflake
koch_snowflake(t, 4, 300)  # Level 4 fractal

# Tunggu hingga jendela ditutup
screen.mainloop()
