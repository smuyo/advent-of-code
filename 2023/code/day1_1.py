import sys

# Create a list for the values
all_vals = []
# For every line in the file
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Create a string with only the digits in it
        pure_line = "".join([charac for charac in line if charac.isdigit()])
        # Add the number with the first and last digits to the list
        all_vals.append(int(pure_line[0] + pure_line[-1]))
# Print the sum of all the values
print(sum(all_vals))
