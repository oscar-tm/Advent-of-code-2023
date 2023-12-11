with open('g:/Programmering/Python/Advent of code/Day 11/input.txt', 'r') as file:
    gMap = []
    rowExpInd = []
    c = 0
    for line in file:
        line = line.strip()
        gMap.append(line)
        if line == line[0] * len(line) and line[0] == '.':
            rowExpInd.append(c)
        c += 1

    j = 0
    colExpInd = []
    while j < len(gMap[0]):
        i = 0
        while i < len(gMap):
            if gMap[i][j] != '.':
                break
            i += 1

        if i == len(gMap):
            colExpInd.append(j)
        j += 1

def getShift(x, expInd):
    c = 0
    for ind in expInd:
        if ind < x:
            c += 1
    return x - c + c * 10**6

gCount = 0
gDict = {}
for i in range(len(gMap)):
    for j in range(len(gMap[i])):
        if gMap[i][j] == "#":
            x = getShift(i, rowExpInd)
            y = getShift(j, colExpInd)
            gDict[gCount] = (x, y)
            gCount += 1
print(gDict)
totDist = 0
seen = set()
for key1, coords1 in gDict.items():
    for key2, coords2 in gDict.items():
        if key1 != key2 and (key1, key2) not in seen:
            totDist += abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
        seen.add((key1, key2))
        seen.add((key2, key1))

print(totDist)