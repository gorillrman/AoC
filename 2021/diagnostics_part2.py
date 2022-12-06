import pandas as pd

#diags = pd.read_csv('diagnostic_input.txt', header=None, dtype=str)
diags = pd.read_csv('diag_test.txt', dtype=str)
diags.columns = ['bins']
diags = diags.astype(str)
oxRatingsList = diags
#oxRatingsList['bins'] = []
coRatingsList = pd.DataFrame()
coRatingsList['bins'] = []
count0 = 0
count1 = 0
oxCount = 0
coCount = 0
gamma = ""
epsilon = ""
# print(len(diags))
# print(oxRatingsList.head())
run = len(diags)
#print('Total run is ', run)
diagLength = len(diags['bins'][0])
#print('Sample length', diagLength)


def oxGen(currentGamma, i, oxRatingsList, coRatingsList):
    for j in range(run):
        print('This is currentGamma:', currentGamma, 'This is compared to currentGamma: ',
              oxRatingsList['bins'][j][i])
        if diags['bins'][j][i] != currentGamma:
            print("We made it")
            oxRatingsList.drop([j])
    print('oxRatings \n', oxRatingsList)
    return(oxRatingsList)


for i in range(diagLength):  # (len(diags)): #run through each position in binary
    if i < run:
        for j in range(run):  # (len(diags)):
            currentDiag = diags['bins'][j]
            #print('Current diag', currentDiag[i])
            if currentDiag[i] == "0":
                count0 = count0 + 1
            elif currentDiag[i] == "1":
                count1 = count1 + 1
            #print('Counts are', count0, count1)
        if count0 > count1:
            print('Count0', count0, 'Count1', count1)
            currentGamma = "0"
            currentEpsilon = "1"
            gamma = gamma + "0"
            epsilon = epsilon + "1"
            oxGen(currentGamma, i, oxRatingsList, coRatingsList)
        else:
            print('Count0', count0, 'Count1', count1)
            currentEpsilon = "0"
            currentGamma = "1"
            gamma = gamma + "1"
            epsilon = epsilon + "0"
            oxGen(currentGamma, i, oxRatingsList, coRatingsList)
        # print(gamma, epsilon)
        # print(int(gamma, 2), int(epsilon, 2))
        # print('Final rate',epsilon*gamma)
        if j > diagLength:
            count0 = 0
            count1 = 0
# print('Gamma is: ', gamma, 'Epsilon is: ', epsilon)
# print('Gamma converted is: ', int(gamma, 2),
#       'Epsilon converted is: ', int(epsilon, 2))
# print('Final rate:', int(gamma, 2) * int(epsilon, 2))

# print('\noxRatings \n', oxRatingsList.head())
