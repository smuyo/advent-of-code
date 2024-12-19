import sys

rules = {}
probs = []

with open(sys.argv[1],'r') as in_file:
    rul_stat = True
    for line in in_file:
        if len(line.rstrip()) == 0:
            rul_stat = False
            continue
        elif rul_stat:
            curr_nums = line.rstrip().split('|')
            try:
                rules[curr_nums[0]][curr_nums[1]] = False
            except:
                rules[curr_nums[0]] = {curr_nums[1]:False}
            try:
                rules[curr_nums[1]][curr_nums[0]] = True
            except:
                rules[curr_nums[1]] = {curr_nums[0]:True}
        else:
            probs.append(line.rstrip().split(','))

num_nums = len(rules)
uncomp_nums = list(rules.keys())
comp_nums = []

while len(uncomp_nums) != len(comp_nums):
    for numb in uncomp_nums:
        if numb not in comp_nums:
            new_nums = {}
            for numb1,asc1 in rules[numb].items():
                for numb2,asc2 in rules[numb1]:
                    if numb2 in rules[numb1]:
                        continue
                    if asc1 == asc2:
                        new_nums[numb2] = asc2
            rules[numb].update(new_nums)
            if len(rules[numb]) == num_nums - 1:
                comp_nums.append(numb)

tot_sum = 0
alt_sum = 0

for problem in probs:
    ord_prob = []
    for numb in problem:
        if len(ord_prob) == 0:
            ord_prob.append(numb)
            continue
        for rev_numb in reversed(range(len(ord_prob))):
            if rules[numb][ord_prob[rev_numb]]:
                ord_prob.insert(rev_numb+1,numb)
                break
            elif rev_numb == 0:
                ord_prob.insert(rev_numb, numb)

    if problem == ord_prob:
        tot_sum += int(problem[int((len(problem) - 1) / 2)])
    else:
        alt_sum += int(ord_prob[int((len(ord_prob) - 1) / 2)])

print(tot_sum)
print(alt_sum)
