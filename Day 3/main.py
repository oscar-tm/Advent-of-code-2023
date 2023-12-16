ans = 0

with open('g:/Programmering/Python/Advent of code/Day 3/test.txt', 'r') as file:
    schmematic = []
    dict = {}
    for line in file:
        schmematic.append(line.strip())

    for j in range(len(schmematic)):
        i = 0
        while i < len(schmematic[j]):
            c = 0
            #Find all gears and adds them to a dictionary containing all the nearby numbers.
            if schmematic[j][i].isnumeric():
                while(i + c < len(schmematic[j]) and schmematic[j][i + c].isnumeric()):
                    c += 1

                if(i + c < len(schmematic[j])):
                    if schmematic[j][i+c] == "*":
                        if not str(j) + str(i+c) in dict:
                            dict[str(j) + str(i+c)] = []
                        dict[str(j) + str(i+c)].append(int(schmematic[j][i : i + c]))
                    rIndex = i + c + 1
                else:
                    rIndex = i + c

                if(i > 0):
                    if schmematic[j][i-1] == "*":
                        if not str(j) + str(i-1) in dict:
                            dict[str(j) + str(i-1)] = []
                        dict[str(j) + str(i-1)].append(int(schmematic[j][i : i + c]))
                    lIndex = i - 1
                else:
                    lIndex = i

                if(j > 0):
                    for k in range(lIndex, rIndex):
                        if schmematic[j-1][k] == "*" and not schmematic[j-1][k].isnumeric():
                            if not str(j-1) + str(k) in dict:
                                dict[str(j-1) + str(k)] = []
                            dict[str(j-1) + str(k)].append(int(schmematic[j][i : i + c]))
                
                if(j < len(schmematic) - 1):
                    for k in range(lIndex, rIndex):
                        if schmematic[j+1][k] == "*" and not schmematic[j+1][k].isnumeric():
                            if not str(j+1) + str(k) in dict:
                                dict[str(j+1) + str(k)] = []
                            dict[str(j+1) + str(k)].append(int(schmematic[j][i : i + c]))

                i += c
            else:
                i += 1

    for gears in dict.values():
        #A gear only have 2 values closeby
        if len(gears) == 2:
            ans += gears[0] * gears[1]

print(ans)