import turtle

def draw_tree(branch_length, angle_left, angle_right, factor, depth):
    if depth == 0:
        return
    turtle.forward(branch_length)
    turtle.left(angle_left)
    draw_tree(branch_length * factor, angle_left, angle_right, factor, depth - 1)
    turtle.right(angle_left + angle_right)
    draw_tree(branch_length * factor, angle_left, angle_right, factor, depth - 1)
    turtle.left(angle_right)
    turtle.backward(branch_length)

def main():
    angle_left = int(input("Left branch angle: "))
    angle_right = int(input("Right branch angle: "))
    start_length = int(input("Starting branch length: "))
    factor = float(input("Branch length reduction factor (e.g., 0.7): "))
    depth = int(input("Recursion depth: "))

    turtle.speed('fastest')
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    draw_tree(start_length, angle_left, angle_right, factor, depth)
    turtle.done()

if __name__ == "__main__":
    main()
