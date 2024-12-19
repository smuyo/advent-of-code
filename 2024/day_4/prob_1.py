import sys

def count_xmas(line_in):
    count = 0
    count += line_in.count("XMAS")
    count += line_in.count("SAMX")
    return(count)


lines = []
curr_line = 0
xmas_total = 0
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        xmas_total += count_xmas(line)
        line_len = len(line.rstrip())
        lines.append(line.rstrip())

for vert in range(line_len):
    curr_line = ''
    for line in lines:
        curr_line += line[vert]
    xmas_total += count_xmas(curr_line)

# Count in diagonal 1
for diag_r in range(line_len):
    curr_line = ''
    for lett in range(len(lines[0][diag_r:])):
        lett_num = lett + diag_r
        curr_line += lines[lett][lett_num]
    xmas_total += count_xmas(curr_line)

num_lines = len(lines)
for diag_r2 in range(1, num_lines):
    curr_line = ''
    for lett2 in range(0, num_lines - diag_r2):
        curr_line += lines[diag_r2 + lett2][lett2]
    xmas_total += count_xmas(curr_line)

# count in diagonal 2
for diag_l in range(num_lines):
    curr_line = ''
    for lett in range(diag_l + 1):
        curr_line += lines[diag_l-lett][lett]
    xmas_total += count_xmas(curr_line)

for diag_l2 in range(1, line_len):
    curr_line = ''
    for lett2 in range(line_len - diag_l2):
        curr_line += lines[-(lett2+1)][diag_l2 + lett2]
    xmas_total += count_xmas(curr_line)

print(xmas_total)
