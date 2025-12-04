size = int(input("Enter the size of the pattern: "))

row = 0

# Use a while loop for each row
while row < size:
    # Use a for loop to print asterisks
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 2
    