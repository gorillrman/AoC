openFile = open('apartmentMap.txt', "r")
openFile = openFile.read()
floorMap = openFile.split()
currentFloor = 0


def splitter(floorMap):
    # print[char for char in floorMap]
    return [char for char in floorMap]


splitter(floorMap)
for i in range(len(floorMap)):
    if i == "(":
        print("Plus 1")
        currentFloor = currentFloor + 1
    elif i == ")":
        print("Minus 1")
        currentFloor = currentFloor - 1
    print(currentFloor)

print(currentFloor)
