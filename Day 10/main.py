q = []
diag = []
sFound = False

with open('g:/Programmering/Python/Advent of code/Day 10/input.txt', 'r') as file:
    for line in file:
        if len(diag) == 0:
            diag.append('.' * len(line))

        diag.append('.' + line.strip() + '.')

        if sFound:
            sFound = False
            if diag[len(diag)-1][sPos] in ['|', 'L', 'J']:
                q.append((len(diag)-2, sPos, 0, 2))

        #Calc The directions to start in
        if 'S' in line:
            if diag[len(diag)-2][line.index('S') + 1] in ['|', '7', 'F']:
                q.append((len(diag)-1, line.index('S') + 1, 0, 0))
            if diag[len(diag)-1][line.index('S') + 2] in ['-', 'J', '7']:
                q.append((len(diag)-1, line.index('S') + 1, 0, 1))
            if diag[len(diag)-1][line.index('S')] in ['-', 'L', 'F']:
                q.append((len(diag)-1, line.index('S') + 1, 0, 3))
            sPos = line.index('S') + 1
            sFound = True
        
    diag.append('.' * len(line))

sPos = q[0][0:2]
order = []
seen = set()
while len(q) != 0:
    #Find the cycle by moving in both directions when they hit eachother we found the farthest place
    currPos = q.pop(0)
    if currPos[0:2] in seen:
        break

    if not currPos[0:2] == sPos:
        seen.add(currPos[0:2])
        order.append(currPos[0:2])

    #Check how to move
    if currPos[3] == 0:
        if diag[currPos[0]-1][currPos[1]] == '|':
            q.append((currPos[0]-1, currPos[1], currPos[2]+1, 0))

        elif diag[currPos[0]-1][currPos[1]] == '7':
            q.append((currPos[0]-1, currPos[1], currPos[2]+1, 3))

        elif diag[currPos[0]-1][currPos[1]] == 'F':
            q.append((currPos[0]-1, currPos[1], currPos[2]+1, 1))

    elif currPos[3] == 1:
        if diag[currPos[0]][currPos[1]+1] == '-':
            q.append((currPos[0], currPos[1]+1, currPos[2]+1, 1))

        elif diag[currPos[0]][currPos[1]+1] == 'J':
            q.append((currPos[0], currPos[1]+1, currPos[2]+1, 0))

        elif diag[currPos[0]][currPos[1]+1] == '7':
            q.append((currPos[0], currPos[1]+1, currPos[2]+1, 2))

    elif currPos[3] == 2:
        if diag[currPos[0]+1][currPos[1]] == '|':
            q.append((currPos[0]+1, currPos[1], currPos[2]+1, 2))

        elif diag[currPos[0]+1][currPos[1]] == 'L':
            q.append((currPos[0]+1, currPos[1], currPos[2]+1, 1))

        elif diag[currPos[0]+1][currPos[1]] == 'J':
            q.append((currPos[0]+1, currPos[1], currPos[2]+1, 3))

    else:
        if diag[currPos[0]][currPos[1]-1] == '-':
            q.append((currPos[0], currPos[1]-1, currPos[2]+1, 3))

        elif diag[currPos[0]][currPos[1]-1] == 'L':
            q.append((currPos[0], currPos[1]-1, currPos[2]+1, 0))

        elif diag[currPos[0]][currPos[1]-1] == 'F':
            q.append((currPos[0], currPos[1]-1, currPos[2]+1, 2))


def containsPoint(verts, coords): #Point in poly alg.
    if coords in seen: #Cannot be on border must be contained within.
        return False
    
    inPoly = False
    i, j = 0, len(verts) - 1
    while i < len(verts) - 1:
        i = i + 1
        if (((verts[i][1] > coords[1]) != (verts[j][1] > coords[1])) and (coords[0] < ((verts[j][0] - verts[i][0]) * (coords[1] - verts[i][1]) / (verts[j][1] - verts[i][1])) + verts[i][0])):
            inPoly = not inPoly
        j = i
    return inPoly

seen.add(sPos)
c = 0
verts = [sPos]
tmp  = []
#Since the algo goes from both dir at the same time need to move everyother element to get correct order
for tup in order:
    if c % 2 == 0:
        verts.append(tup)
    else:
        tmp.append(tup)
    c += 1

verts += tmp[::-1]
ans = 0
for x in range(len(diag)):
    for y in range(len(diag[x])):
        if containsPoint(verts, (x, y)):
            ans += 1

print(ans)