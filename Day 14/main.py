dish = []

with open('g:/Programmering/Python/Advent of code 2023/Day 14/input.txt', 'r') as file:
    for line in file:
        dish.append(list(line.strip()))

#Convert the char to int values
mapDict = {'.' : 0, '#' : 1, 'O' : 2}
for i in range(len(dish)):
    for j in range(len(dish[i])):
        dish[i][j] = mapDict[dish[i][j]]

def north(dish):
    #Executes a north tilt
    for j in range(len(dish[0])):
        for i in range(len(dish)):
            if dish[i][j] == 2:
                c = 1
                while i-c >= 0 and dish[i-c][j] == 0:
                    dish[i-c][j] = 2
                    dish[i-c+1][j] = 0
                    c += 1
    return dish

def south(dish):
    #Executes a southtilt by reversing then calling north then reverings again.
    dish = dish[::-1]
    dish = north(dish)
    dish = dish[::-1]
    return dish

def east(dish):
    #Executs a east tile by transposing then doing a south call then transposing again.
    dish = [list(x) for x in zip(*dish)]
    dish = south(dish)
    dish = [list(x) for x in zip(*dish)]
    return dish

def west(dish):
    #Executes a west tilt be transposing the matrix then doing north then transposing again
    dish = [list(x) for x in zip(*dish)]
    dish = north(dish)
    dish = [list(x) for x in zip(*dish)]
    return dish

def load(dish):
    #Calculates the current north load of the dish
    ans = 0
    for i in range(len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == 2:
                ans += len(dish) - i
    return ans

import time
s = time.time()
cState = tuple(tuple(x) for x in dish)
seen = {}
loads = [0]
i = 1
while cState not in seen: #While we are in a state we havent seen to a tilt cycle
    seen[cState] = i

    dish = north(dish)
    dish = west(dish)
    dish = south(dish)
    dish = east(dish)
    loads.append(load(dish))

    cState = tuple(tuple(x) for x in dish)
    i += 1

#The cycle len is the current nCycle - the last time we saw the current state
cycleLen = i - seen[cState]
#The shift is simply the first time we saw the current state
shift = seen[cState]

print(loads[shift + (1000000000 - shift) % cycleLen])
print(time.time() - s)