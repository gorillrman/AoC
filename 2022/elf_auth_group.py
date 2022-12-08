import pandas as pd
import datetime as dt

current_date = dt.datetime.now()
date_label = current_date.strftime("%m%d%Y_%H%M%S")
#snacks = open("elf_priority_data.txt", "r")
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
print(left_right)
temp_match = []
matcher = []
group1 = []
group2 = []
group3 = []


def checkMatch(auth1, auth2):
    for k in auth1:
        for l in auth2:
            if k == l and k not in temp_match:
                temp_match.append(k)
    return temp_match


def checkSecondMatch(temp_match, auth3):
    for i in temp_match:
        for k in auth3:
            if k in temp_match:
                matcher.append(k)
                temp_match = []
                temp_list = []
                return matcher


for i in range(0, len(snackers), 3):
    #i = i.strip()
    auth1 = snackers[i].strip()
    auth2 = snackers[i+1].strip()
    auth3 = snackers[i+2].strip()
    temp_list = [auth1, auth2, auth3]
    group1.append(auth1)
    group2.append(auth2)
    group3.append(auth3)
    for j in temp_list:
        temp_match = []
        checkMatch(auth1, auth2)
    checkSecondMatch(temp_match, auth3)

left_right['group1'] = group1
left_right['group2'] = group2
left_right['group3'] = group3
left_right['matches'] = matcher
left_right.to_csv("left_right_"+date_label+".csv", index=False)
print(left_right.head())
for i in matcher:
    adder = crazy_alpha.index(i)+1
    # print(i,adder)
    totaler = adder + totaler
    print(totaler)

    #     compartments_left.append(priority1)
    #     compartments_right.append(priority2)
    #     for i in priority1:
    #         for j in priority2:
    #             if i == j and i not in current_matches:
    #                 current_matches.append(i)
    #         # print(current_matches)
    #     for i in current_matches:
    #         split_match.append(i)
    #         current_matches = []

    # for i in split_match:
    #     adder = crazy_alpha.index(i)+1
    #     # print(i,adder)
    #     totaler = adder + totaler

    # left_right['left'] = compartments_left
    # left_right['right'] = compartments_right
    # left_right['match'] = split_match
    # left_right.to_csv("left_right_"+date_label+".csv", index=False)
    # print(totaler)
