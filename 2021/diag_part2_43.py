# importing needed modules
import numpy
from numpy.core.numeric import NaN
import pandas as pd

# importing data list
oxDiags = pd.read_csv('E:\OneDrive\Programmy\Python\AoC\\2021\diag_test.csv', names=[
    'binaries'], header=None, dtype=str)
# oxDiags = pd.read_csv('E:\OneDrive\Programmy\Python\AoC\\2021\diagnostic_input.txt', names=[
#                       'binaries'], header=None, dtype=str)

coDiags = oxDiags
# variables
count0 = 0
count1 = 0
i = 0
diagPos = len(oxDiags['binaries'][0])


def counter(diagers, diagPos):
    while len(diagers) > 1:
        run1 = len(diagers)
        if i < diagPos:  # iterate over dataframe
            for j in range(run1):
                currentDiag = oxDiags['binaries'][j]
                if str(currentDiag[i]) == "0":
                    count0 = count0 + 1
                elif str(currentDiag[i]) == "1":
                    count1 = count1 + 1


# iterate through dataframe to remove
while len(oxDiags) > 1 or len(coDiags) > 1:
    run1 = len(oxDiags)
    run2 = len(coDiags)
    if i < diagPos:  # iterate over dataframe
        for j in range(run1):
            currentDiag = oxDiags['binaries'][j]
            if str(currentDiag[i]) == "0":
                count0 = count0 + 1
            elif str(currentDiag[i]) == "1":
                count1 = count1 + 1
    if count0 > count1 and len(oxDiags) > 1:
        if len(oxDiags) == 1:
            continue
        for k in range(len(oxDiags)):
            if str(oxDiags['binaries'][k][i]) == "1":
                try:
                    oxDiags = oxDiags.drop(k)
                except:
                    print("Nope")
        for k in range(len(coDiags)):
            if str(coDiags['binaries'][k][i]) == "0":
                try:
                    coDiags = coDiags.drop(k)
                except:
                    print("Nope")
    elif count1 > count0:
        for k in range(len(oxDiags)):
            if len(oxDiags) == 1:
                continue
            if str(oxDiags['binaries'][k][i]) == "0":
                try:
                    oxDiags = oxDiags.drop(k)
                except:
                    print("Nope")
        for k in range(len(coDiags)):
            if len(coDiags) == 1:
                continue
            if str(coDiags['binaries'][k][i]) == "1":
                try:
                    coDiags = coDiags.drop(k)
                except:
                    print("Nope")

    elif count1 == count0:
        for k in range(len(oxDiags)):
            if len(oxDiags) == 1:
                continue
            if str(oxDiags['binaries'][k][i]) == "0":
                try:
                    oxDiags = oxDiags.drop(k)
                except:
                    print("Nope")
        for k in range(len(coDiags)):
            if len(coDiags) == 1:
                continue
            if str(coDiags['binaries'][k][i]) == "1":
                try:
                    coDiags = coDiags.drop(k)
                except:
                    print("Nope")
    i += 1
    oxDiags = oxDiags.reset_index(drop=True)
    coDiags = coDiags.reset_index(drop=True)
    count0 = 0
    count1 = 0
    # i = 0

print('Oxygen Scrubber', oxDiags)
print('CO2 Scrubbers', coDiags)
# finalOx = int(oxDiags, 2)
print(int(oxDiags['binaries'][0], 2))
print('final', int(oxDiags['binaries'][0], 2)*int(coDiags['binaries'][0], 2))
