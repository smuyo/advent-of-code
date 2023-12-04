import sys

# Create a list for the values
all_vals = []
# Create the dictionary for the substitutions
numbers = {"one":"o1n1e", "two":"t2w2o", "three":"t3hre3e", "four":"f4ou4r", "five":"f5iv5e", "six":"s6i6x", "seven":"s7eve7n", "eight":"e8igh8t", "nine":"n9in9e"}
# For every line in the file
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Translate the written digits
        for digi_writ in numbers:
            line = line.replace(digi_writ, numbers[digi_writ])
        # Create the string with only the digits in it
        pure_line = "".join([charac for charac in line if charac.isdigit()])
        # Add the number with the first and last digits to the list
        all_vals.append(int(pure_line[0] + pure_line[-1]))

# Print the sum of all the values
print(sum(all_vals))
