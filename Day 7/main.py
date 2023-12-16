from functools import cmp_to_key

card2Num = {"A" : 14, "K" : 13, "Q" : 12, "J" : 1, "T" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}

def evaluteHand(hand):
    #Evalutes a hand with Jokers
    count = {}
    containsJ = False
    for char in hand[0]:
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1

        if char == "J":
            containsJ = True

    if not containsJ:
        count["J"] = 0

    counts = []
    for key, v in count.items():
        if key != "J":
            counts.append(v)
    
    counts.sort(reverse=True)
    try:
        counts[0] += count["J"]
    except IndexError:
        counts.append(count["J"])

    return evaluteHandNoJ(counts)


def evaluteHandNoJ(count):
    #Evalutes a hand where jokers have a set value
    v = count

    if len(count) == 1:
        return 6
    elif len(count) == 2:
        if v[0] == 4 or v[1] == 4:
            return 5
        else:
            return 4
    elif len(count) == 3:
        if v[0] == 3 or v[1] == 3 or v[2] == 3:
            return 3
        else:
            return 2
    elif len(count) == 4:
        return 1
    else:
        return 0

def compareHands(hand1, hand2):
    #Compares two hands
    hand1, hand2 = hand1[0], hand2[0]
    for i in range(len(hand1)):
        diff = card2Num[hand1[i]] - card2Num[hand2[i]]
        if diff == 0:
            continue
        return diff
    return 0

with open('g:/Programmering/Python/Advent of code/Day 7/input.txt', 'r') as file:
    hands = []
    for line in file:
        tmp = line.strip().split(" ")
        hands.append([tmp[0], int(tmp[1])])

handDict = {6 : [], 5 : [], 4 : [], 3 : [], 2 : [], 1 : [], 0 : []}

for hand in hands:
    handDict[evaluteHand(hand)].append(hand)

handsInOrder = []
for handList in handDict.values():
    handsInOrder += sorted(handList, key = cmp_to_key(compareHands), reverse = True)

handsInOrder = handsInOrder[::-1]
totalWinnings = 0

for i in range(len(handsInOrder)):
    totalWinnings += handsInOrder[i][1]*(i+1)

print(totalWinnings)