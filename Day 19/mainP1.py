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
        for cond in self.condList:
            if cond[1]:
                if x[cond[0]] > cond[2]:
                    return cond[-1]

            else:
                if x[cond[0]] < cond[2]:
                    return cond[-1]
                
        return self.default

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

    workflows['R'] = 0
    workflows['A'] = 1

    for line in file:
        line = line.strip()[1:-1]
        line = [x.split('=') for x in line.split(',')]
        tmp = {}
        for cat in line:
            tmp[cat[0]] = int(cat[1])

        parts.append(tmp)

ans = 0
for part in parts:
    workflow = workflows['in']
    while True:
        if workflow == 0 or workflow == 1:
            break
        
        workflow = workflows[workflow.calc(part)]

    if workflow == 1:
        ans += sum(part.values())

print(ans)