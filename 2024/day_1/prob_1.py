import sys

left = []
right = []

with open(sys.argv[1]) as data_in:
    for line in data_in:
        curr_nums = line.split()
        left.append(curr_nums[0])
        right.append(curr_nums[-1])

left.sort()
right.sort()

total_sum = 0

for numbi in range(len(left)):
    total_sum += abs(int(left[numbi]) - int(right[numbi]))

print(total_sum)