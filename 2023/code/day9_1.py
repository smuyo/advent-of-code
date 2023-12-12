import sys


def step_compute(in_list):
    new_list = []
    if all(v == 0 for v in in_list):
        cur_res = 0
    else:
        for pair in range(1, len(in_list)):
            new_list.append(in_list[pair] - in_list[pair - 1])
        
        res_upper = step_compute(new_list)

        cur_res = new_list[-1] + res_upper
    
    return cur_res

values = 0
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        start_vals = list(map(int, line.strip().split()))
        values += start_vals[-1] + step_compute(start_vals)

print(values)