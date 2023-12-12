import sys
import math

def find_steps(start_str, dir_dict):
    steps = 0
    reach_end = False
    while not reach_end:
        for i in instructions:
            # print(i)
            # print(start_ele)
            # print(dirs[start_ele]) 
            steps += 1
            if i == "R":
                start_str = dir_dict[start_str][1]
            elif i == "L":
                start_str = dir_dict[start_str][0]
            
            if start_str[-1] == "Z":
                reach_end = True
                break
    return steps

start_line = True
dirs = {}
start_eles = []
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        if start_line:
            instructions = line.strip()
            start_line = False
        else:
            if len(line) > 1:
                eles = line.strip().split(" = ")
                dirs[eles[0]] = eles[1][1:-1].split(", ")
                if eles[0][-1] == "A":
                    start_eles.append(eles[0])

steps_nums = []
for start_loc in start_eles:
    steps_nums.append(find_steps(start_loc, dirs))
print(math.lcm(*steps_nums))