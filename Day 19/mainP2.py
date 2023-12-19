class Cond:
    def __init__(self, conds):
        self.condList = []
        for cond in conds[:-1]:
            if cond[1] == '<':
                self.condList.append((cond[0], False, int(cond[2:cond.find(':')]), cond[cond.find(':')+1:]))
            else:
                self.condList.append((cond[0], True, int(cond[2:cond.find(':')]), cond[cond.find(':')+1:]))

        self.default = conds[-1]

    def calc(self, x):
        parts = []
        newPart = x
        for key, op, threshold, nWorkflow in self.condList:
            if op:
                tmp = self.copyDict(newPart)
                newPart[key][0] = threshold + 1
                parts.append([nWorkflow, newPart])
                newPart = tmp
                newPart[key][1] = threshold

            else:
                tmp = self.copyDict(newPart)
                newPart[key][1] = threshold - 1
                parts.append([nWorkflow, newPart])
                newPart = tmp
                newPart[key][0] = threshold
                
        parts.append([self.default, newPart])
        return parts
    
    def copyDict(self, dic):
        nDic = {}
        for key, value in dic.items():
            nDic[key] = value.copy()
        return nDic

with open('g:/Programmering/Python/Advent of code 2023/Day 19/input.txt', 'r') as file:
    workflows = {}
    parts = []

    for line in file:
        if not line.strip():
            break
        line = line.strip()
        workflowID = line[:line.find('{')]
        conds = line[line.find('{')+1:-1].split(',')
        
        workflows[workflowID] = Cond(conds)

parts = [['in', {'x' : [1, 4000], 'm' : [1, 4000], 'a' : [1, 4000], 's' : [1, 4000]}]]
finshedRanges = []
while len(parts) > 0:
    tmp = []
    for part in parts:
        if part[0] == 'R' or part[0] == 'A':
            finshedRanges.append(part)
            continue
        tmp = tmp + workflows[part[0]].calc(part[1])
    parts = tmp

ans = 0
for r in finshedRanges:
    if r[0] == 'A':
        tmp = 1
        for cr in r[1].values():
            if cr[1] - cr[0] + 1 < 0:
                tmp = 0
                break
            tmp = tmp * (cr[1] - cr[0]+1)
        ans += tmp
print(ans)