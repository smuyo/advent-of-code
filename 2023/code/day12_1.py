import sys



def rec_check(curr_space, last_chars, rem_groups):
    if len(curr_space) == 0:
        if len(rem_groups) > 0:
            return 0
        else:
            return 1
    
    else:
        if curr_space[0] == ".":
            return rec_check(curr_space[1:], 0, rem_groups)
        elif curr_space[0] == "#":
            if last_chars + 1 == rem_groups[0]:
                return 1 + rec_check(curr_space[1:], last_chars +1, rem_groups) 


tot_opts = 0
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        fields = line.strip().split()
        conds = list(map(int, fields[1].split(",")))
        row = fields[0]
        num_damaged = row.count("#")
        if num_damaged == sum(conds):
            tot_opts += 1
            continue
        
        else:

