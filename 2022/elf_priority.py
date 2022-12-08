import pandas as pd
import datetime as dt

current_date = dt.datetime.now()
date_label = current_date.strftime("%m%d%Y_%H%M%S")
snacks = open("elf_priority_data.txt", "r")
snackers = snacks.readlines()
split_compartment = []
split_match = []
totaler = 0
compartments_left = []
compartments_right = []
crazy_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
               "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
current_matches = []
left_right = pd.DataFrame()

for i in snackers:
    i = i.strip()
    priority1 = i[:len(i)//2]
    priority2 = i[len(i)//2:]
    compartments_left.append(priority1)
    compartments_right.append(priority2)
    for i in priority1:
        for j in priority2:
            if i == j and i not in current_matches:
                current_matches.append(i)
        # print(current_matches)
    for i in current_matches:
        split_match.append(i)
        current_matches = []

for i in split_match:
    adder = crazy_alpha.index(i)+1
    # print(i,adder)
    totaler = adder + totaler

left_right['left'] = compartments_left
left_right['right'] = compartments_right
left_right['match'] = split_match
left_right.to_csv("left_right_"+date_label+".csv", index=False)
print(totaler)
