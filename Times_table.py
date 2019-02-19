import turtle as t
from time import sleep

t.speed(0)
t.screensize(1200, 1200)

num_pts = 200
step_length = 10
left_angle = 360 / (num_pts)

coords = {}

def set():
    t.pu()
    t.goto(0, -270)
    t.pd()

def circle():
    set()
    t.pencolor("blue")
    for i in range(num_pts+1):
        coords[i] = t.pos()
        t.fd(step_length)
        t.lt(left_angle)
    set()

def draw(n):
    for x in range(2, n+1):
        circle()
        t.pencolor("green")
        for i in range(num_pts+1):
            t.pu()
            t.goto(coords[i])
            t.pd()
            target = (i * x) % num_pts
            t.goto(coords[target])
        sleep(1.5)
        t.clear()

def main():
    n = int(input("Enter number of types of figures: "))
    draw(n)

if __name__ == "__main__":
    main()

t.exitonclick()
