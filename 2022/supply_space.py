import pandas as pd
import datetime as dt

current_date = dt.datetime.now()
date_label = current_date.strftime("%m%d%Y_%H%M%S")
#supply_list = open("supply_space_sample_data.txt", "r")
supply_list = open("supply_space_data.txt", "r")
supplies = supply_list.readlines()
supply_start1 = []
supply_end1 = []
supply_start2 = []
supply_end2 = []
start_end = ""
counter = 0
counted = []
results = pd.DataFrame()
second_group = False


for i in supplies:
    for j in i:
        if j != "-" and j != "," and j != "\n":
            start_end = str(start_end) + str(j)
        elif j == "-":
            start_end = int(start_end)
            if second_group:
                supply_start2.append(start_end)
            else:
                supply_start1.append(start_end)
            start_end = ""
        elif j == ",":
            start_end = int(start_end)
            supply_end1.append(start_end)
            start_end = ""
            second_group = True
        else:
            start_end = int(start_end)
            supply_end2.append(start_end)
            start_end = ""
            second_group = False

supply_end2.append(int(start_end))
start_end = ""

for i in range(len(supply_start1)):
    if supply_start1[i] <= supply_start2[i] and supply_end1[i] >= supply_end2[i]:
        counter += 1
        counted.append(1)
    elif supply_start2[i] <= supply_start1[i] and supply_end2[i] >= supply_end1[i]:
        counter += 1
        counted.append(1)
    else:
        counted.append(0)

results['start1'] = supply_start1
results['end1'] = supply_end1
results['start2'] = supply_start2
results['end2'] = supply_end2
results['result'] = counted
print('counted', len(counted))
results.to_csv("supply_results_"+date_label+".csv", index=False)

print('counter', counter)
