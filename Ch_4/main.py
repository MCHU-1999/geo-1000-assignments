import turtle

def square(turtle_obj: turtle.Turtle):
    for i in range(4):
        turtle_obj.forward(200)
        turtle_obj.lt(90)

if __name__ == '__main__':
    bob = turtle.Turtle()
    square(bob)
    # print(bob)
    turtle.mainloop()