import sys

# Create the list for the output
out_list = []
# For every line in the file
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Reset the current prize and create lists for our numbers and the winner numbers
        curr_prize = 0
        line_nums = line.split(":")[1].strip()
        winning = line_nums.split("|")[0].strip().split(" ")
        our_numbers = line_nums.split("|")[1].strip().split(" ")

        # For every number we got
        for number in our_numbers:
            # If it is a winner (the first statement is a not so nice way of avoiding a problem with single digit numbers)
            if number != '' and number in winning:
                # Increase the prize
                if curr_prize == 0:
                    curr_prize += 1
                else:
                    curr_prize *= 2
        # Add the final prize to the list
        out_list.append(curr_prize)

# Print the final prize
print(sum(out_list))