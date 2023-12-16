import math

def firstDigit(string):
    #Find index of first digit
    for i in range(len(string)):
        if string[i].isdigit():
            return i
    return -1

with open('g:/Programmering/Python/Advent of code/Day 6/input.txt', 'r') as file:
    #Load the data
    time = []
    num = ""
    line = file.readline().strip()
    i = firstDigit(line)
    while i < len(line):
        while i < len(line) and line[i].isdigit():
            num += line[i]
            i += 1
        if num != "":
            time.append(int(num))
        num = ""
        i += 1

    dist = []
    num = ""
    line = file.readline().strip()
    i = firstDigit(line)
    while i < len(line):
        while i < len(line) and line[i].isdigit():
            num += line[i]
            i += 1
        if num != "":
            dist.append(int(num))
        num = ""
        i += 1

ans = 1
#Calc ways to win
for i in range(len(time)):
    tmp = 0
    for t in range(1, time[i]):
        dM = t*(time[i]-t)
        if dM > dist[i]:
            tmp += 1

    ans *= tmp

print(ans)

time = int("".join(str(n) for n in time))
dist = int("".join(str(n) for n in dist))

lb = math.floor(time/2 - math.sqrt((time**2)/4 - dist))
ub = math.floor(time/2 + math.sqrt((time**2)/4 - dist))

ans = ub - lb

print(ans)