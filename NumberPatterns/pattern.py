# Program to print a pyramid number pattern

# Function to print pyramid pattern
def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + " ".join(str(j) for j in range(1, i + 1)))

# Taking input for the number of rows
rows = int(input("Enter the number of rows: "))

# Calling the function
pyramid_pattern(rows)

# Function to print inverted pyramid pattern
def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + " ".join(str(j) for j in range(1, i + 1)))

print("\nInverted Pyramid:")
inverted_pyramid(rows)

def right_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

print("\nRight-Aligned Triangle:")
right_aligned_triangle(rows)

