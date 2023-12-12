import sys
from collections import Counter

cat_dict = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}}
sort_order = "AKQT98765432J"
prize = 0

with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        fields = line.strip().split()
        char_num = Counter(fields[0])
        
        if "J" in char_num:
            base_rank = char_num["J"]
            del char_num["J"]
        else:
            base_rank = 0
        
        if len(char_num) == 0:
            curr_max = 5
            num_occ = 1
        else:
            char_counts = Counter(char_num.values())
            curr_max = max(char_counts.keys())
            num_occ = char_counts[curr_max]
            if num_occ == 1:
                del char_counts[curr_max]
            curr_max += base_rank

        if curr_max == 5:
            cat_dict[6][fields[0]] = fields[1]
        elif curr_max == 4:
            cat_dict[5][fields[0]] = fields[1]
        elif curr_max == 3:
            if 2 in char_counts:
                cat_dict[4][fields[0]] = fields[1]
            else:
                cat_dict[3][fields[0]] = fields[1]
        elif curr_max == 2:
            if 2 in char_counts:
                cat_dict[2][fields[0]] = fields[1]
            else:
                cat_dict[1][fields[0]] = fields[1]
        else:
            cat_dict[0][fields[0]] = fields[1]

curr_rank = 1
for cat in range(len(cat_dict)):
    # print(cat_dict[cat])
    comb_order = sorted(cat_dict[cat], key=lambda word: [sort_order.index(char) for char in word], reverse = True)
    for comb in comb_order:
        print(comb, cat_dict[cat][comb])
        prize += int(cat_dict[cat][comb]) * curr_rank
        curr_rank += 1

print(prize)

