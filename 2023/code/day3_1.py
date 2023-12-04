import sys
import re

# Create required objects
prev_nums = {}
prev_chars = []
out_nums = []

# For every line
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Create some more objects (for the numbers that pass, the symbols and the numbers of the current line)
        passing = {}
        curr_chars = []
        curr_nums = {}
        line = line.strip()
        # Add the positions of the symbols to the list of current symbols
        for charac_num in range(len(line)):
            charac = line[charac_num]
            if not charac.isdigit() and charac != ".":
                curr_chars.append(charac_num)
        # Search for numbers in the line and add them and their coordinates to the dict
        line_nums = re.finditer(r'\d+', line)
        for number in line_nums:
            curr_number = number.group()
            curr_coords = number.span()
            if curr_number not in curr_nums:
                curr_nums[curr_number] = [curr_coords]
            else:
                curr_nums[curr_number].append(curr_coords)
        
        # If there are some numbers left from the previous line
        for numb in prev_nums:
            for coord_set in range(len(prev_nums[numb])):
                curr_coords = prev_nums[numb][coord_set]
                for char in curr_chars:
                    # Check if some character in the current line can "save" them and if it does add the number to the output list
                    if (curr_coords[0] - 1) <= char <= (curr_coords[1]):
                        out_nums.append(int(numb))
                        break

        # For every number from the current line
        for numb2 in curr_nums:
            for coord_set in range(len(curr_nums[numb2])):
                pass_stat = False
                curr_coords = curr_nums[numb2][coord_set]
                # Check if it's next to a symbol
                for char in curr_chars:
                    if (curr_coords[0] - 1) <= char <= (curr_coords[1]):
                        # If it is, add it to the output list
                        out_nums.append(int(numb2))
                        # And add the number and the coordinates to the passing dictionary
                        if numb2 not in passing:
                            passing[numb2] = [coord_set]
                        else:
                            passing[numb2].append(coord_set)
                        pass_stat = True
                        break
                # If the number has not passed the test and there were some symbols in the previous line
                if not pass_stat and len(prev_chars) > 0:
                    for char2 in prev_chars:
                        # If the symbol saves the number add it to the output list and add the coordinates to the passing dict
                        if (curr_coords[0] - 1) <= char2 <= (curr_coords[1]):
                            if numb2 not in passing:
                                passing[numb2] = [coord_set]
                            else:
                                passing[numb2].append(coord_set)
                            out_nums.append(int(numb2))
                            break
        # Remove every number that passed the test in the current line
        for numb3 in passing:
            for i in sorted(passing[numb3], reverse=True):
                del curr_nums[numb3][i]
            if len(curr_nums[numb3]) == 0:
                del curr_nums[numb3]
        # Store the numbers that are left and the characters of this line for the next iteration
        prev_nums = curr_nums
        prev_chars = curr_chars
print(out_nums)
print(sum(out_nums))
        