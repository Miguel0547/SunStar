"""
CSAPX Lab 2: Sun Star

A program that draws a sun star with s sides, each side length n, v levels, and deviation angle θ
To draw a sun star side of length n, level v, and deviation angle θ,
1. Draw a line of length n/4.
2. Turn θ degrees to the left.
3. Draw a sun star side of length (n/4)/cosθ and level v − 1.
4. Repeat the above in a way that creates the mirror image of what was already drawn

Variables accepted in this program will be of either type int or float

author: Miguel Reyes
date: 09/05/21
"""
import math
import turtle


# This function defines the pre-conditions for the turtle object(my preference for where I'd like to begin on the
# canvas)
def init_conditions():
    turtle.speed(4)
    turtle.penup()
    turtle.setx(-50)
    turtle.sety(0)
    turtle.pendown()
    turtle.left(90)


def draw_side(length: float, angle: float, levels: int, sum=0) -> float:
    """
    Recursive Function for drawing one sided shapes.

    This will draw one side of the sun star and returns its total length - for every move the turtle makes,
    the length of that move is stored and updated into the sum variable allowing us to calculate the total length of
    all lines combined.

    :param length: The length of one side in pixels (the level-1 equivalent length)

    :param angle: The angle measurement that is used when the turtle is turning left or right. Also, used in
    the formula to calculate the length of every new line segment ( (length/4) / cos(angle) )

    :param levels: this is the depth of the sun star. At level-1 the turtle will draw a straight line, otherwise it will
    draw the next segments of line using a recursive call to draw_side

    :param sum: Will calculate and store each new line created

    :return float: Total of length of all lines combined(sum variable)
    """
    # At level 1 the turtle object will only move forward by length(px) and then it returns the length measurement. The
    # function then ends.
    if levels == 1:
        turtle.forward(length)
        sum += length
    # For every move the turtle makes, the length of that move is stored and updated into the sum variable allowing
    # us to calculate the total length of all lines combined
    else:

        # Step 1) Starts facing 0deg, moves forward length/4
        turtle.forward(length / 4)
        sum += length / 4
        # Step 2) Turn left angle deg
        turtle.left(angle)
        # Step 3) Here the the nth line segment is created - every recursive call will subtract 1 from its depth to
        # move on to new line segment
        sum += draw_side((length / 4) / math.cos(math.radians(angle)), angle, levels - 1)
        # Step 4) Turn twice the original angle
        turtle.right(angle * 2)
        # Here the nth + 1 line segment is created - every recursive call will subtract 1 from its depth to move on
        # to the very last parts of the shape which is a left(angle) turn and a move forward by length / 4
        # This recursive call mirrors the first lines created in Steps 1-4 creating that vertically symmetric shape
        sum += draw_side((length / 4) / math.cos(math.radians(angle)), angle, levels - 1)
        # Last steps I mentioned in the previous comment
        turtle.left(angle)
        turtle.forward(length / 4)
        sum += length / 4

    return sum


def draw_sides(length: float, angle: float, levels: int, num_sides: int) -> float:
    """
    ***I did not use recursion for this function because a TA announced on our Discussion board that we could use
    a for loop instead.***

    This function will call the draw_side function in a for loop(i = 0  to (num_sides - 1)) as well as turn right
    at (360 /num_sides) allowing to create a the full sun star -  closed shape

    The function will return the draw side() total length * num_sides because that will be the new total of lines
    created. Ex)If draw_side returns a total length of 200 and we're calling this function and passing a num-sides
    of 2 then we are creating the one-sided sun star from draw_side() twice therefore its perimeter will double.

    :param length: will be the length from draw_side()
    :param angle: will be the angle from draw_side()
    :param levels: will be the levels from draw_sides()
    :param num_sides: the number of shapes to create
    :return float: Total of length of all lines combined(draw_side(x,y,z) * num_sides)
    """

    for i in range(num_sides - 1):
        draw_side(length, angle, levels)
        turtle.right(360 / num_sides)
    return draw_side(length, angle, levels) * num_sides


def main():
    # use while loop & exception handling to check if the user enters the data type correctly
    # - if incorrect will prompt user until its correct
    while True:
        try:
            num_sides = int(input("Enter number of sides ? "))
            break
        except ValueError:
            print("You entered an incorrect value - value must be a int.")
            continue
    # use while loop & exception handling to check if the user enters the data type correctly
    # - if incorrect will prompt user until its correct
    while True:
        try:
            length = float(input("Enter length of initial side ? "))
            break
        except ValueError:
            print("You entered an incorrect value - value must be a float.")
            continue
    # use while loop & exception handling to check if the user enters the data type correctly
    # - if incorrect will prompt user until its correct
    while True:
        try:
            levels = int(input("Enter number of levels ? "))
            break
        except ValueError:
            print("You entered an incorrect value - value must be a int.")
            continue
    # here levels > 1 but only 1 side so it will draw only one side of the sun star
    if levels > 1 and num_sides == 1:
        # use while loop & exception handling to check if the user enters the data type correctly
        # - if incorrect will prompt user until its correct
        while True:
            try:
                angle = float(input("Enter deflection angle ? "))
                break
            except ValueError:
                print("You entered an incorrect value - value must be a float.")
                continue
        init_conditions()
        print("Total length: " + str(draw_side(length, angle, levels)) + " pixels.")
        turtle.mainloop()
    # here levels & num_sides > 1 so it will create an enclosed sun-star the size of the one-sided sun-star * num_sides
    elif levels > 1 and num_sides > 1:
        # use while loop & exception handling to check if the user enters the data type correctly
        # - if incorrect will prompt user until its correct
        while True:
            try:
                angle = float(input("Enter deflection angle ? "))
                break
            except ValueError:
                print("You entered an incorrect value - value must be a float.")
                continue
        init_conditions()
        print("Total length: " + str(draw_sides(length, angle, levels, num_sides)) + " pixels.")
        turtle.mainloop()
    # Here levels == 1 so it will only create a straight line of length entered by user
    elif levels == 1:
        angle = 0
        init_conditions()
        print("Total length: " + str(draw_side(length, angle, levels)) + " pixels.")
        turtle.mainloop()
    # Inputs for sides and levels of 0 will result in ending the program
    else:
        pass

# only run this program if it is not being imported by another main module
if __name__ == "__main__":
    main()
