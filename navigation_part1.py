# imports
import pandas as pd

# create navigation instructions dataframe
navInstructions = pd.read_csv('navigation.txt', sep=" ", header=None)
navInstructions.columns = ['direction', 'steps']

# variables for tracking location
horizontal = 0
depth = 0

for i in range(len(navInstructions)):
    if navInstructions['direction'][i] == 'forward':
        horizontal = horizontal + navInstructions['steps'][i]
    elif navInstructions['direction'][i] == 'down':
        depth = depth + navInstructions['steps'][i]
    else:
        depth = depth - navInstructions['steps'][i]
    print(depth, horizontal)

location = horizontal * depth
print(location)
