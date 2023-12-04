import sys
import math

out = []
# For every line in the input file
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Separate the try from the info
        id_info = line.split(":")
        # Store the try number
        curr_id = id_info[0].split(" ")[1]
        # Separate each time the elf showed us something
        tries = id_info[1].split(";")
        # Create a dict with the current maximum
        curr_max = {"red":0, "green":0, "blue":0}
        # For every showing
        for curr_try in tries:
            # Split the informations, and for every bit
            curr_info = curr_try.split(",")
            for info in curr_info:
                info = info.strip()
                info_num = int(info.split(" ")[0])
                # Check the number of balls for every color
                if "red" in info and info_num > curr_max["red"]:
                    curr_max["red"] = info_num
                elif "green" in info and info_num > curr_max["green"]:
                    curr_max["green"] = info_num
                elif "blue" in info and info_num > curr_max["blue"]:
                    curr_max["blue"] = info_num

        # Append the game id to the list
        out.append(math.prod(curr_max.values()))
# Sum all the ids of the possible games and print the result
print(sum(out))
