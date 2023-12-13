def findReflection(m):
    refs = []
    for i in range(len(m[0])-1):
        c = 1
        ref = True
        smudge = 0
        while(0 <= i + 1 - c and i + c < len(m[0])):
            for j in range(len(m)):
                if m[j][i + 1 - c] != m[j][i+c]:
                    if smudge == 0:
                        smudge += 1
                    else:
                        ref = False
                        break
            if ref:
                c += 1
            else:
                break
                
        if ref and (i + 1 - c == -1 or i + c == len(m[0])) and smudge == 1:
            refs.append(i+1)
    return refs

def transpose(m):
    return [list(x) for x in zip(*m)]

with open('g:/Programmering/Python/Advent of code 2023/Day 13/input.txt', 'r') as file:
    m = []
    ans = 0
    for line in file:
        line = line.strip()
        if line:
            m.append(line)
        else:
            for ref in findReflection(m):
                ans += ref
            for ref in findReflection(transpose(m)):
                ans += ref*100
            m = []

    for ref in findReflection(m):
        ans += ref
    for ref in findReflection(transpose(m)):
        ans += ref*100

print(ans)