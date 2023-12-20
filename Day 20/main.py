from math import lcm

modDict = {}

with open('g:/Programmering/Python/Advent of code 2023/Day 20/input.txt', 'r') as file:
    modules = []
    for line in file:
        line = line.strip().split(' -> ')
        if line[0] == 'broadcaster':
            start = line[1].split(', ')
            modules.append(['', line[0], start])

        else:
            modules.append([line[0][0], line[0][1:], line[1].split(', ')])


for type, name, con in modules:
    if name == 'broadcaster':
        continue
    pInput = []
    inputDict = {}
    i = 0
    for _, name2, con2 in modules:
        if name == name2:
            continue

        if name in con2:
            pInput.append(False)
            inputDict[name2] = i
            i += 1

    if type == '%':
        isFlipFlop = True
    else:
        isFlipFlop = False
    modDict[name] = (pInput, con, inputDict, isFlipFlop)

q = []
for sPos in start:
    q.append((sPos, False, None)) #False low signal, True high signal

cycleCheck = [False, False, False, False]
nHigh = 0
nLow = 1 + len(start)
cycleLen = 1
subcycleLens = []
while len(q) > 0:
    cState, cSig, pState = q.pop(0)
    
    try:
        states, con, stateMap, flipFlop = modDict[cState]

        if flipFlop:
            if not cSig:
                nSig = not modDict[cState][0][0]
                modDict[cState][0][0] = nSig
                for conState in con:
                    q.append((conState, nSig, cState))

                if nSig:
                    nHigh += len(con)

                else:
                    nLow += len(con)

        else:
            modDict[cState][0][modDict[cState][2][pState]] = cSig
            if all(states):
                nSig = False

            else:
                nSig = True

            for conState in con:
                q.append((conState, nSig, cState))

            if nSig:
                nHigh += len(con)

            else:
                nLow += len(con)

    except KeyError:
        if cState == 'rx' and not cSig:
            break
    
    #We get the subcycle id's by inspecting our input data
    if not cycleCheck[0] and all(modDict['mf'][0]):
        cycleCheck[0] = True
        subcycleLens.append(cycleLen)

    if not cycleCheck[1] and all(modDict['ph'][0]):
        cycleCheck[1] = True
        subcycleLens.append(cycleLen)

    if not cycleCheck[2] and all(modDict['zp'][0]):
        cycleCheck[2] = True
        subcycleLens.append(cycleLen)

    if not cycleCheck[3] and all(modDict['jn'][0]):
        cycleCheck[3] = True
        subcycleLens.append(cycleLen)

    if len(q) == 0: #Recheck that it has reverted to inital values otherwise add start again!
        end = True
        for mod in modDict.values():
            if any(mod[0]):
                end = False
                break
        if not end:
            cycleLen += 1
            for sPos in start:
                q.append((sPos, False, None))
            nLow += 1 + len(start)

        # if cycleLen == 1001:
        #     cycleLen = 1000
        #     nLow -= 1 + len(start)
        #     print(nHigh, nLow, cycleLen)
        #     print(nHigh * nLow * (1000/cycleLen) ** 2)
        #     break

        if all(cycleCheck): #If we have found all the subcycles, the answer is the lcm.
            print(lcm(*subcycleLens))
            break