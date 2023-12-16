with open("/Users/oscar/Programmering/Python/Advent-of-code-2023/Day 16/input.txt", 'r') as file:
    #Open file and save all the data in matrix
    contraption = []
    energized = []
    for line in file:
        contraption.append(line.strip())
        energized.append([0]*len(line.strip()))

def getNewDir(pos):
    #Calculates the new direction for / can be taken as -getNewDir(pos) for \
    if pos[1][0] == 1:
        return (0, -1)
    elif pos[1][0] == -1:
        return (0, 1)
    elif pos[1][1] == 1:
        return (-1, 0)
    else:
        return (1, 0)

def calcRef(start):
    queue = [start]
    seen = set()
    while len(queue) > 0:
        pos = queue.pop(0) # [(x, y), (dx, dy)]

        if pos in seen:
            continue

        seen.add(pos)

        #If we are outside of the border skip
        if not (0 <= pos[0][0] + pos[1][0] < len(contraption[0])) or not (0 <= pos[0][1] + pos[1][1] < len(contraption)):
            continue

        #Check what reflection to calc
        if contraption[pos[0][1] + pos[1][1]][pos[0][0] + pos[1][0]] == '|':
            if pos[1][1] != 0:
                queue.append(((pos[0][0], pos[0][1] + pos[1][1]), (pos[1][0], pos[1][1])))
            else:
                queue.append(((pos[0][0] + pos[1][0], pos[0][1]), (0, -1)))
                queue.append(((pos[0][0] + pos[1][0], pos[0][1]), (0, 1)))

        elif contraption[pos[0][1] + pos[1][1]][pos[0][0] + pos[1][0]] == '-':
            if pos[1][0] != 0:
                queue.append(((pos[0][0] + pos[1][0], pos[0][1]), (pos[1][0], pos[1][1])))
            else:
                queue.append(((pos[0][0], pos[0][1] + pos[1][1]), (1, 0)))
                queue.append(((pos[0][0], pos[0][1] + pos[1][1]), (-1, 0)))

        elif contraption[pos[0][1] + pos[1][1]][pos[0][0] + pos[1][0]] == '.':
            queue.append(((pos[0][0] + pos[1][0], pos[0][1] + pos[1][1]), (pos[1][0], pos[1][1])))

        elif contraption[pos[0][1] + pos[1][1]][pos[0][0] + pos[1][0]] == '/':
            newDir = getNewDir(pos)
            queue.append(((pos[0][0] + pos[1][0], pos[0][1] + pos[1][1]), newDir))

        else:
            newDir = getNewDir(pos)
            queue.append(((pos[0][0] + pos[1][0], pos[0][1] + pos[1][1]), (-newDir[0], -newDir[1])))
        
        energized[pos[0][1] + pos[1][1]][pos[0][0] + pos[1][0]] = 1

def calcEnergized():
    #Sum the energized matrix
    ans = 0
    for l in energized:
        for val in l:
            ans += val
    return ans

ans = 0
#All possible startes
for y in range(-1, len(contraption) + 1):
    for x in range(-1, len(contraption[0]) + 1):
        #If we are diagonal of the corner of within the contraption skip
        if x == y and (x == -1 or x == len(contraption[0])) or (x != -1 and x != len(contraption) and y != -1 and y != len(contraption)):
            continue

        energized = [[0]*len(contraption) for _ in range(len(contraption))]
        if x == -1:
            startPos = ((x, y), (1, 0))
        elif x == len(contraption):
            startPos = ((x, y), (-1, 0))
        elif y == -1:
            startPos = ((x, y), (0, 1))
        else:
            startPos = ((x, y), (0, -1))

        calcRef(startPos)
        ans = max(ans, calcEnergized())

print(ans)