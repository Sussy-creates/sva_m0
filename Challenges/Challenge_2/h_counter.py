# This script is completing challenge 2 from module 0, static void
# The following program will count the letters 'H' and 'h' from an input, and output the resutl

# Obtaining using input and assigning it
sign = input("Input message: ")

# setting up variables used to count letters
NUM_H = 0
num_h = 0

# Counting letters
for char in sign:
        if char == "H":
            NUM_H += 1
        elif char == "h":
            num_h += 1

# Outputting results
print(f"H: {NUM_H}, h: {num_h}")

