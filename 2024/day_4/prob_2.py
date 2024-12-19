import sys

lines = []

with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        lines.append(line.rstrip())

xmas_num = 0

for line in range(1, len(lines) - 1):
    for lett in range(1, len(lines[line]) - 1):
        if lines[line][lett] == 'A':
            diag1 = lines[line-1][lett-1] + lines[line+1][lett+1]
            diag2 = lines[line+1][lett-1] + lines[line-1][lett+1]
            if (diag1 == 'MS' or diag1 == 'SM') and (diag2 == 'MS' or diag2 == 'SM'):
                xmas_num += 1

print(xmas_num)
