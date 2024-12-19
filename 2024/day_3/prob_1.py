import sys
import re

multi_res = 0
with open(sys.argv[1], "r") as in_data:
    for line in in_data:
        split_1 = [a + ")" for a in line.split(")")]
        split_line = []
        for test_str in split_1:
            split_line += ["mul(" + b for b in test_str.split("mul(")]
        for str_test in split_line:
            
            if "mul(" in str_test and str_test[-1] == ")" and len(str_test) > 7 and len(str_test) < 13:
                test_nums = str_test[4:-1].split(",")
                if len(test_nums) == 2:
                    try:
                        multi_res += int(test_nums[0]) * int(test_nums[1])
                    except:
                        continue

print(multi_res)