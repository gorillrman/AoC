import pandas as pd

diags = pd.read_csv('diagnostic_input.txt', header=None, dtype=str)
#diags = pd.read_csv('diag_test.txt', header=None, dtype=str)

diags.columns = ['bins']
diags = diags.astype(str)
count0 = 0
count1 = 0
gamma = ""
epsilon = ""
# print(len(diags))
# print(diags.head())
run = len(diags)
print('Total run is ', run)
diagLength = len(diags['bins'][0])
print('Sample length', diagLength)


def countDiag():
    nothing = 'nothing'


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
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        # print(gamma, epsilon)
        # print(int(gamma, 2), int(epsilon, 2))
        # print('Final rate',epsilon*gamma)
        if j > diagLength:
           #print("resetting counters now")
            count0 = 0
            count1 = 0
print('Gamma is: ', gamma, 'Epsilon is: ', epsilon)
print('Gamma converted is: ', int(gamma, 2),
      'Epsilon converted is: ', int(epsilon, 2))
print('Final rate:', int(gamma, 2) * int(epsilon, 2))
