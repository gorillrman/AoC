#! /usr/bin/env python3
# Sean McKenna test scripting (2021)

# importing needed modules
import numpy
from numpy.core.numeric import NaN
import pandas as pd


# variables
counting = 0
count0 = 0
colNames = []
colCounts = pd.DataFrame()
# importing data list first is for testing, second is real data
oxDiags = pd.read_csv(
    "E:\OneDrive\Programmy\Python\AoC\\2021\diag_test.csv",
    names=["binaries"],
    header=None,
    dtype=str,
)
# oxDiags = pd.read_csv('E:\OneDrive\Programmy\Python\AoC\\2021\diagnostic_input.txt', names=[
#                       'binaries'], header=None, dtype=str)


oxDiags = oxDiags["binaries"].str.split(pat="\s*", expand=True)
oxDiags = oxDiags.iloc[:, 1:-1]

oxDiags.columns = range(oxDiags.shape[1])

# getting totals for columns in current dataframe
def counter():
    global colCounts
    for i in colNames:
        colCounts = colCounts.append(oxDiags[i].value_counts())
    print(colCounts)


# looking to drop non-dominant rows in dataframe
def dropper(cols):
    global oxDiags
    for index, row in colCounts.iterrows():
        if row[0] > row[1]:
            for j in range(len(oxDiags)):
                if int(oxDiags[cols][j]) == 1:
                    oxDiags = oxDiags.drop(int(oxDiags[cols][j]))
                    print("printing", oxDiags[cols][j])
                else:
                    print("Not working", oxDiags[cols])


# getting list of columns in oxDiags dataframe
def getCols():
    for col in oxDiags.columns:
        colNames.append(col)
    return colNames


def main():
    ox = True
    getCols()
    for cols in colNames:
        counterThis = counter()
        dropper(cols)
    return


if __name__ == "__main__":
    main()
