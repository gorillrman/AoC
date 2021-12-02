# import pandas to create datafram
import pandas as pd
from pandas.core.indexes.base import Index

# Read file into dataframe.
depth = pd.read_csv('depth.txt', sep=" ", header=None)
depth = pd.DataFrame(depth)
depth.columns = ['depths']
# print(depth)
increase = 0

# function to add depth windows


def findCurrentDepth(d, i):
    # create globals to pass back to main
    global depth1
    global depth2
    # initialize variables
    depth1 = 0
    depth2 = 0
    # iterate through adding depths
    for finder in range(3):
        print(depth['depths'][i])
        depth1 = depth1 + depth['depths'][i]
        depth2 = depth2 + depth['depths'][d]
        i = i+1
        d = d+1
    return(depth1, depth2)


for i in range(len(depth)):
    d = i+1
    if d < len(depth)-2:
        newDepths = findCurrentDepth(d, i)
        if depth2 > depth1:
            #print(d, i)
            increase = increase + 1
        # print(increase)

print(increase)
