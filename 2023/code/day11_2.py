import sys

start = True
num_line = 0
galaxies = []
empty_lines = []
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        
        if start:
            empty_cols = {x:True for x in range(len(line.strip()))}
            start = False

        if "#" in line:
            for char_loc in range(len(line.strip())):
                char = line[char_loc]
                if char == "#":
                    if char_loc in empty_cols:
                        del empty_cols[char_loc]
                    galaxies.append([num_line, char_loc])
        
        else:
            empty_lines.append(num_line)
        
        num_line += 1

total_dist = 0
num_pairs = 0
for start_g in range(len(galaxies)):
    s_line = galaxies[start_g][0]
    s_col = galaxies[start_g][1]
    for end_g in range(start_g, len(galaxies)):
        e_line = galaxies[end_g][0]
        e_col = galaxies[end_g][1]
        if e_col < s_col:
            small_col = e_col
            big_col = s_col
        else:
            small_col = s_col
            big_col = e_col
        
        if e_line < s_line:
            small_line = e_line
            big_line = s_line
        else:
            small_line = s_line
            big_line = e_line
        curr_dist = 0
        curr_dist += big_line - small_line
        curr_dist += big_col - small_col
        for column in range(small_col, big_col):
            if column in empty_cols:
                curr_dist += 999999
        for line in range(small_line, big_line):
            if line in empty_lines:
                curr_dist += 999999
        total_dist += curr_dist
print(total_dist)