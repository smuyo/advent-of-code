
import sys

start_line = True
dirs = {}
start_ele = "AAA"
last_ele = "ZZZ"
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        if start_line:
            instructions = line.strip()
            start_line = False
        else:
            if len(line) > 1:
                eles = line.strip().split(" = ")
                dirs[eles[0]] = eles[1][1:-1].split(", ")

steps = 0
reach_end = False
while not reach_end:
    for i in instructions:
        # print(i)
        # print(start_ele)
        # print(dirs[start_ele]) 
        steps += 1
        if i == "R":
            start_ele = dirs[start_ele][1]
        elif i == "L":
            start_ele = dirs[start_ele][0]
        
        if start_ele == last_ele:
            reach_end = True
            break

print(steps)