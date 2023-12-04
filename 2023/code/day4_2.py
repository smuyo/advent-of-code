import sys

num_info = {}

# For every line in the file
with open(sys.argv[1], "r") as in_file:
    for line in in_file:
        # Reset the current prize and create lists for our numbers and the winner numbers
        curr_card = line.split(":")[0].strip().split(" ")[-1]
        line_nums = line.split(":")[1].strip()
        winning = line_nums.split("|")[0].strip().split(" ")
        our_numbers = line_nums.split("|")[1].strip().split(" ")
        num_info[int(curr_card)] = {"winners": winning, "numbers":our_numbers, "copies":1}

total_cards = 0
for card in num_info:
    print(card, num_info[card]["copies"])
    for copy in range(num_info[card]["copies"]):
        total_cards += 1
        curr_prize = 0
        # For every number we got
        for number in num_info[card]["numbers"]:
            # If it is a winner (the first statement is a not so nice way of avoiding a problem with single digit numbers)
            if number != '' and number in num_info[card]["winners"]:
                # Increase the prize
                curr_prize += 1
        for prize_card in range(card + 1, card + 1 + curr_prize):
            num_info[prize_card]["copies"] += 1

# Print the final prize
print(total_cards)