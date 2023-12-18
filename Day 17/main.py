import heapq

with open('g:/Programmering/Python/Advent of code 2023/Day 17/input.txt', 'r') as file:
    cityMap = []
    for line in file:
        cityMap.append(line.strip())

possibleDirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    start = (0, 0, 0, -1)
    q = []
    seen = {}
    
    best = 10000000000
    heapq.heappush(q, start)
    while len(q) > 0:
        cHLoss, x, y, pDir = heapq.heappop(q)

        if (x, y) == (len(cityMap) - 1, len(cityMap) - 1):
            best = min(best, cHLoss)
            continue
   
        for i in range(4):
            if (i % 4 == pDir or (i + 2) % 4 == pDir):
                continue
            
            nHLoss = cHLoss
            #The neighbours in Djikstras are going left or right for 1 - 11 steps
            for j in range(1, 11):
                nX = x + possibleDirs[i][0] * j
                nY = y + possibleDirs[i][1] * j
                if 0 <= nX < len(cityMap) and 0 <= nY < len(cityMap):
                    nHLoss += int(cityMap[nY][nX])
                    if j > 3:
                        if (nX, nY, i) not in seen:
                            seen[(nX, nY, i)] = nHLoss
                            heapq.heappush(q, (nHLoss, nX, nY, i))

                        else:
                            if nHLoss < seen[(nX, nY, i)]:
                                seen[(nX, nY, i)] = nHLoss
                                heapq.heappush(q, (nHLoss, nX, nY, i))

    return best

print(bfs())