from functools import cache

with open('g:/Programmering/Python/Advent of code 2023/Day 12/input.txt', 'r') as file:
    records = []
    groups = []
    for line in file:
        line = line.strip().split()
        line[1] = [int(x) for x in line[1].split(',')]
        tmp = line[0]
        tmp1 = line[1].copy()
        for i in range(4):
            line[0] += "?" + tmp
            line[1] += tmp1
        records.append(line[0])
        groups.append(line[1])

ans = 0
combRecords = list(zip(records, groups))
mapping = {'.' : 0, "#" : 1, "?" : 2}

@cache
def dp(record, group, prevChar, rI, gI, cLen):
    if rI == len(record) and len(group) - 1 <= gI <= len(group):
        if gI == len(group) - 1:
            if cLen == group[gI]:
                return 1
            else:
                return 0
        if cLen == 0:
            return 1
        else:
            return 0
    elif rI >= len(record) or (gI >= len(group) and record[rI] == 1):
        return 0

    if gI < len(group) and cLen == group[gI]:
        if record[rI] != 1:
            return dp(record, group, 0, rI + 1, gI + 1, 0)
        else:
            return 0

    if record[rI] == 0:
        if prevChar == 0:
            return dp(record, group, 0, rI + 1, gI, 0)
        else:
            if gI < len(group) and cLen == group[gI]:
                return dp(record, group, 0, rI + 1, gI + 1, 0)
            return 0

    if record[rI] == 1:
        return dp(record, group, 1, rI + 1, gI, cLen + 1)

    ans = 0
    for i in range(2):
        if i == 0:
            if prevChar == 1:
                if gI < len(group) and cLen == group[gI]:
                    ans += dp(record, group, i, rI + 1, gI + 1, 0)
            else:
                ans += dp(record, group, i, rI + 1, gI, 0)
        else:
            ans += dp(record, group, i, rI + 1, gI, cLen + 1)

    return ans

n = 0
for record, group in combRecords:
    record = tuple([mapping[char] for char in record])
    group = tuple(group)
    n += dp(record, group, 0, 0, 0, 0)

print(n)