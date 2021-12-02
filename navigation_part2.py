# imports
import pandas as pd

# create navigation instructions dataframe
navInstructions = pd.read_csv('navigation.txt', sep=" ", header=None)
navInstructions.columns = ['direction', 'steps']

# variables for tracking location
horizontal = 0
depth = 0
aim = 0


def aimer(aim):
    currentAim = aim


for i in range(len(navInstructions)):
    if navInstructions['direction'][i] == 'forward':
        horizontal = horizontal + navInstructions['steps'][i]
        if aim != 0:
            depth = depth + navInstructions['steps'][i]*aim
    elif navInstructions['direction'][i] == 'down':
        depth = depth + navInstructions['steps'][i]
        aim = aim + navInstructions['steps'][i]
        #aim = aimer(aim)

    else:
        depth = depth - navInstructions['steps'][i]
        aim = aim - navInstructions['steps'][i]
    print(aim)

location = depth * horizontal
print(location)
