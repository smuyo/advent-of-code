import sys

# Set the limits and create a list for the tries that pass
limits = {"red":12, "green":13, "blue":14}
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
        possible = True
        # For every showing
        for curr_try in tries:
            # Create a dict with the current maximum
            curr_max = {"red":0, "green":0, "blue":0}
            # Split the informations, and for every bit
            curr_info = curr_try.split(",")
            for info in curr_info:
                info = info.strip()
                # Check the number of balls for every color
                if "red" in info:
                    curr_max["red"] += int(info.split(" ")[0])
                elif "green" in info:
                    curr_max["green"] += int(info.split(" ")[0])
                elif "blue" in info:
                    curr_max["blue"] += int(info.split(" ")[0])
            # If any number of balls exceeded the limits, set the possible to false and break the for loop
            if (curr_max["red"] > limits["red"]) or (curr_max["green"] > limits["green"]) or (curr_max["blue"] > limits["blue"]):
                possible = False
                break
            else:
                continue
        # If the game was possible, append the game id to the list
        if possible:
            out.append(int(curr_id))
# Sum all the ids of the possible games and print the result
print(sum(out))
