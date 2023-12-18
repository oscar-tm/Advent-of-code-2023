with open('g:/Programmering/Python/Advent of code 2023/Day 18/input.txt', 'r') as file:
    cPos = (0,0)
    circ = 0
    pDirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    coords = [cPos]
    for line in file:
        line = line.strip().split(" ")

        line[2] = line[2][2:-1]

        cDir = int(line[2][-1])
        steps = int(line[2][:-1], 16)

        cPos = (cPos[0] + pDirs[cDir][0] * steps, cPos[1] + pDirs[cDir][1] * steps)
        coords.append(cPos)
        circ += steps

def shoeLaceFormula(coords):
    area = 0
    for i in range(len(coords)-1):
        area += (coords[i][0] * coords[i + 1][1] - coords[i + 1][0] * coords[i][1])
    return 1/2 * area

"""
Due to the fact that when count the area of a polygong we want to put our point in the middle of the index.
This leads us to miss 1/2 of the circumfuruence when calculating the area of the polygon. Furthermore when
we calc the area we also miss 1 a.u. due to the fact when we go arount the polygon the total sum of angles
will be 360 thus we need to add 1 to our answer.
"""
print(shoeLaceFormula(coords) + circ/2 + 1)