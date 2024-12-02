import sys

left = []
right = []

with open(sys.argv[1]) as data_in:
    for line in data_in:
        curr_nums = line.split()
        left.append(curr_nums[0])
        right.append(curr_nums[-1])

score = 0

for numbi in left:
    score += int(numbi) * right.count(numbi)

print(score)