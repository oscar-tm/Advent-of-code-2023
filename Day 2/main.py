from operator import mul
from functools import reduce

with open('g:/Programmering/Python/Advent of code/Day 2/input.txt', 'r') as file:
    ans = 0
    for line in file:
        nDict = {'red' : 0, 'green' : 0, 'blue' : 0}
        possible = True
        line = line[line.find(':') + 1:] #Remove 'Game x: ' from line
        line = line.split(";")
        for game in line:
            game = game.split(",")
            for colour in game:
                colour = colour.strip()
                colour = colour.split(" ")
                if int(colour[0]) > nDict[colour[1]]:
                    nDict[colour[1]] = int(colour[0])
        #Calcs the power of a set
        ans += reduce(mul, nDict.values(), 1)

print(ans)