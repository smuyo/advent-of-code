import sys

safe_reps = 0

with open(sys.argv[1]) as in_data:
    for line in in_data:
        # print(line)
        decr = ''
        prev_num = False
        curr_nums = line.split()
        error_stat = 0
        for numbi in curr_nums:
            # print("------ new num ------")
            # print(numbi)
            curr_num = int(numbi)
            if prev_num:
                curr_diff = curr_num - prev_num
                # print(curr_num, prev_num, curr_diff)
                if (curr_diff == 0) or (abs(curr_diff) > 3):
                    error_stat += 1
                    break
                elif decr == '':
                    if curr_diff > 0:
                        decr = False
                    else:
                        decr = True
                else:
                    # print(decr)
                    # print(curr_diff)
                    if ((decr == True) and (curr_diff > 0)) or ((decr == False) and (curr_diff < 0)):
                        error_stat = True
                        break
            prev_num = curr_num
        print(error_stat)
        if not error_stat:
            safe_reps += 1

print(safe_reps)