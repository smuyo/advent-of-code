import sys
import copy

def check_line(in_list):
    decr = []
    for v,w in zip(in_list[:-1],in_list[1:]):
        if w == v:
            return(False)
            
        curr_diff = int(w) - int(v)
        
        if abs(curr_diff) > 3:
            return(False)
        
        if curr_diff < 0:
            decr.append(True)
        else:
            decr.append(False)
    
    if not all(x == decr[0] for x in decr):
        return(False)
    
    return(True)




safe_reps = 0

with open(sys.argv[1]) as in_data:
    for line in in_data:
        curr_nums = line.split()
        
        if check_line(curr_nums):
            safe_reps += 1
        else:
            for i in range(len(curr_nums)):
                new_nums = copy.deepcopy(curr_nums)
                new_nums.pop(i)
                
                if check_line(new_nums):
                    safe_reps += 1
                    break

print(safe_reps)