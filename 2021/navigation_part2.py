# imports
import pandas as pd

# create navigation instructions dataframe
navInstructions = pd.read_csv('navigation.txt', sep=" ", header=None)
#navInstructions = pd.read_csv('nav_test.txt', sep=" ", header=None)
navInstructions.columns = ['direction', 'steps']

# variables for tracking location
horizontal = 0
depth = 0
aim = 0

for i in range(len(navInstructions)):
    if navInstructions['direction'][i] == 'forward':
        horizontal = horizontal + navInstructions['steps'][i]
        if aim != 0:
            depth = depth + navInstructions['steps'][i]*aim
    elif navInstructions['direction'][i] == 'down':
        aim = aim + navInstructions['steps'][i]
    else:
        aim = aim - navInstructions['steps'][i]
    print(aim, depth)

location = depth * horizontal
print(location)
