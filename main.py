import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','pink','white','brown']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%9])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
    