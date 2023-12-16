from math import gcd

letter2Num = {"L" : 0, "R" : 1}
target = "ZZZ"

with open('g:/Programmering/Python/Advent of code/Day 8/input.txt', 'r') as file:
    instruction = file.readline().strip()
    file.readline()
    nodeNetwork = dict()
    startNodes = []

    #Load file and collect relevant data
    for line in file:
        node, connectedNodes = line.strip().split(" = ")
        node = node.strip()

        lNode, rNode = connectedNodes.split(", ")
        lNode = lNode[1:]
        rNode = rNode[:-1]

        nodeNetwork[node] = [lNode, rNode]

        if node[2] == 'A':
            startNodes.append(node)

def lcm(integers):
    #Least common multiple gives the correct answer
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // gcd(a, b)
    return a

cNode = "AAA"
res = []
for cNode in startNodes:
    i = 0
    while(cNode[2] != "Z"):
        cNode = nodeNetwork[cNode][letter2Num[instruction[i % len(instruction)]]]
        i += 1
    res.append(i)

print(lcm(res))