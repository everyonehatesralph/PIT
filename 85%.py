# Import necessary modules
import turtle  # Import the turtle graphics library
from random import randint  # Import the randint function from the random module for generating random numbers

# Input racer names and the bet
name1 = input("Name for Racer 1: ")  # Prompt the user to enter a name for Racer 1 and store it in the 'name1' variable
name2 = input("Name for Racer 2: ")  # Prompt the user to enter a name for Racer 2 and store it in the 'name2' variable
bet = input(f"Please pick one player for your bet? \n[{name1}] or [{name2}]\nJust Type the name of your bet: ")  # Prompt the user to make a bet on one of the racers and store it in the 'bet' variable

# Set variables for screen and race configuration
screen_title = 'TURTLE DRAG RACE'  # Set the title of the game
t1_color = 'Red'  # Define the color for Racer 1
t2_color = 'Blue'  # Define the color for Racer 2
BgColor = 'Black'  # Set the background color of the game
distance = 250  # Define the coordinate of the distance from the start to the finish line
W_tur = 650  # Set the width of the screen using the 'W_tur' variable
H_tur = 180  # Set the height of the screen using the 'H_tur' variable
turtle_shape = 'turtle'  # Define the shape of the turtle graphics

# Screen layout
display = turtle.Screen()  # Create a turtle graphics screen
display.setup(W_tur, H_tur)  # Set up the screen with the specified width and height
display.bgcolor(BgColor)  # Set the background color of the screen

# Create the finish line
fin_line = turtle.Turtle()  # Create a turtle object for the finish line
fin_line.color('White')  # Set the color of the finish line to white
fin_line.shape('square')  # Set the shape of the finish line to a square
fin_line.penup()  # Lift the pen to prevent drawing when moving the turtle

# Loop to draw a checkered finish line
for i in range(5):
    fin_line.goto(250, (85 - (i * 20 * 2)))  # Move to the specified position and draw a stamp
    fin_line.stamp()

for j in range(4):
    fin_line.goto(250 + 20, ((85 - 20) - (j * 20 * 2)))  # Move to the specified position and draw a stamp
    fin_line.stamp()

# The Onscreen title
title = turtle.Turtle()  # Create a turtle object for the onscreen title
title.goto(-100, 50)  # Move the title turtle to the specified position
title.pencolor('White')  # Set the color of the pen (used for writing) to white
title.write(screen_title, font=("Arial", 15, "normal"))  # Write the screen title with the specified font
title.hideturtle()  # Hide the title turtle

# Create two turtle objects for the racers
T1 = turtle.Turtle()  # Create a turtle object for Racer 1
T2 = turtle.Turtle()  # Create a turtle object for Racer 2

# Set up and display racer information for Racer 1
R1 = turtle.Turtle()  # Create a turtle object for displaying Racer 1's information
R1.hideturtle()  # Hide the Racer 1 turtle
R1.penup()  # Lift the pen to prevent drawing when moving the turtle
R1.goto(-290, 10)  # Move to the specified position to display Racer 1's name
R1.color(t1_color)  # Set the color of the pen for writing
R1.write(name1, font=("Arial", 15, "normal"))  # Write Racer 1's name with the specified font

T1.shape(turtle_shape)  # Set the shape of the turtle graphics for Racer 1
T1.color(t1_color)  # Set the color of the turtle graphics for Racer 1
T1.penup()  # Lift the pen to prevent drawing
T1.goto(-200, 20)  # Move Racer 1's turtle to the specified starting position
T1.penup()  # Lift the pen again

# Set up and display racer information for Racer 2
R2 = turtle.Turtle()  # Create a turtle object for displaying Racer 2's information
R2.hideturtle()  # Hide the Racer 2 turtle
R2.penup()  # Lift the pen to prevent drawing
R2.goto(-290, -30)  # Move to the specified position to display Racer 2's name
R2.color(t2_color)  # Set the color of the pen for writing
R2.write(name2, font=("Arial", 15, "normal"))  # Write Racer 2's name with the specified font

T2.shape(turtle_shape)  # Set the shape of the turtle graphics for Racer 2
T2.color(t2_color)  # Set the color of the turtle graphics for Racer 2
T2.color()  # (Note: This line seems to have no effect and can be removed)
T2.penup()  # Lift the pen to prevent drawing
T2.goto(-200, -20)  # Move Racer 2's turtle to the specified starting position
T2.penup()  # Lift the pen again

# Simulate the race
for i in range(250):  # Loop for simulating the race
    T1.forward(randint(1, 5))  # Move Racer 1's turtle forward by a random distance
    T2.forward(randint(1, 5))  # Move Racer 2's turtle forward by a random distance

    if T1.xcor() >= distance or T2.xcor() >= distance:
        break  # If either racer crosses the finish line, exit the loop

# Determine the winner
if T1.xcor() >= distance and T2.xcor() >= distance:  # If both racers cross the finish line simultaneously
    print("It's a tie!")  # Print that it's a tie
elif T1.xcor() >= distance:  # If Racer 1 crosses the finish line
    if bet == name1:  # If the bet matches Racer 1
        print(f"\nCongratulations! You won against {name2}.\nYou win the bet on Racer 1!")  # Print a winning message
    elif bet != name1:  # If the bet doesn't match Racer 1
        print("\nYOU BET WHO?!\nThere's only 2 players.\n  Please Try Again.")  # Print an error message
    else:  # If none of the above conditions are met
        print(f"\n{name1} wins, but you lost your bet on Turtle 2.")  # Print a message about Racer 1 winning, but the bet being lost on Racer 2
elif T2.xcor() >= distance:  # If Racer 2 crosses the finish line
    if bet == name2:  # If the bet matches Racer 2
        print(f"\nCongratulations! You won against {name1}.\nYou win the bet on Racer 2!")  # Print a winning message
    elif bet != name2:  # If the bet doesn't match Racer 2
        print("\nYou Bet Who?!\nThere's only 2 players.\n  Please Try Again.")  # Print an error message
    else:  # If none of the above conditions are met
        print(f"\n{name2} wins, but you lost your bet on Racer 1.")  # Print a message about Racer 2 winning, but the bet being lost on Racer 1

# End of the game
print("\nRace and Bet again!\nEnjoy the Game!!")  # Print a message indicating the end of the game

# Close the turtle graphics window when clicked
turtle.exitonclick()  # Allow the user to close the graphics window by clicking on it
