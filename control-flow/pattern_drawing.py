# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate over each row
while row < size:
    # Use a for loop to print stars in the current row
    for column in range(size):
        print("*", end="")  # end="" keeps it on the same line
    print()  # Print a newline after each row
    row += 1  # Move to the next row
