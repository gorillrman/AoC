# importing Pandas to create dataframe
import numpy
from numpy.core.numeric import NaN
import pandas as pd
# importing data list
diags = pd.read_csv('E:\OneDrive\Programmy\Python\AoC\\2021\diag_test.csv', names=[
                    'binaries'], header=None, dtype=str)
# diags = pd.read_csv('diagnostic_input.txt', names=[binaries'], header=None, dtype=str)
oxRatingList = diags
coRatingList = diags
newoxRating = []
newcoRating = []
run = len(diags)
diagLength = len(diags['binaries'][0])
count0 = 0
count1 = 0
oxygen = ""
co2 = ""

# Getting counts from diagnostic list
for i in range(len(oxRatingList)):  # iterate over first character of each binary
    if i < run:  # iterate over dataframe
        for j in range(run):
            currentDiag = oxRatingList['binaries'][j]
            if str(currentDiag[i]) == "0":
                count0 = count0 + 1
            elif str(currentDiag[i]) == "1":
                count1 = count1 + 1
        if count0 > count1:
            if len(oxRatingList) > 1:
                for k in range(len(oxRatingList)):
                    if oxRatingList[k][i] != 0:
                        oxRatingList.drop(k)
            if len(coRatingList) > 1:
                if coRatingList[k][i] != 1:
                    try:
                        newcoRating.append(coRatingList[k])
                    except:
                        print("CO2 drop didn't work")
        # else:
        #     if len(oxRatingList) > 1:
        #         for k in range(len(oxRatingList)):
        #             if oxRatingList['binaries'][k][i] == "0":
        #                 try:
        #                     newoxRating.append(oxRatingList['binaries'][k])
        #                 except:
        #                     print("Ox Drop didn't work")
        #             if coRatingList['binaries'][k][i] == "1":
        #                 try:
        #                     newcoRating.append(oxRatingList['binaries'][k])
        #                 except:
        #                     print("CO2 drop didn't work")
        # oxRatingList['binaries'] = pd.Series(newoxRating)
        # coRatingList['binaries'] = pd.Series(newcoRating)
        # oxRatingList = oxRatingList['binaries'].dropna()
        # coRatingList = coRatingList['binaries'].dropna()
        # oxRatingList.columns = ['binaries']
        # coRatingList.columns = ['binaries']
        # newoxRating = []
        # newcoRating = []
