import sys
from collections import Counter

cat_dict = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}}
sort_order = "AKQJT98765432"
prize = 0

with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        fields = line.strip().split()
        char_counts = Counter(Counter(fields[0]).values())
        if 5 in char_counts:
            cat_dict[6][fields[0]] = fields[1]
        elif 4 in char_counts:
            cat_dict[5][fields[0]] = fields[1]
        elif 3 in char_counts:
            if 2 in char_counts:
                cat_dict[4][fields[0]] = fields[1]
            else:
                cat_dict[3][fields[0]] = fields[1]
        elif 2 in char_counts:
            if char_counts[2] == 2:
                cat_dict[2][fields[0]] = fields[1]
            else:
                cat_dict[1][fields[0]] = fields[1]
        else:
            cat_dict[0][fields[0]] = fields[1]

curr_rank = 1
for cat in range(len(cat_dict)):
    comb_order = sorted(cat_dict[cat], key=lambda word: [sort_order.index(char) for char in word], reverse = True)
    for comb in comb_order:
        prize += int(cat_dict[cat][comb]) * curr_rank
        curr_rank += 1

print(prize)

