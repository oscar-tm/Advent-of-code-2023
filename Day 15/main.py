def hashFunc(seq):
    hashValue = 0
    for char in seq:
        if char in "-=":
            break
        hashValue += ord(char)
        hashValue = (hashValue * 17) % 256
    return hashValue

with open("/Users/oscar/Programmering/Python/Advent-of-code-2023/Day 15/input.txt", 'r') as file:
    line = file.readline().strip().split(',')

boxes = [[] for _ in range(256)]
boxesSets = [set() for _ in range(256)]
for seq in line:
    box = hashFunc(seq)
    if seq[-1] == '-':
        seq = seq[:-1]
        if seq in boxesSets[box]:
            boxesSets[box].remove(seq)
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == seq:
                    boxes[box].pop(i)
                    break

    else:
        seq = seq.split('=')
        if seq[0] in boxesSets[box]:
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == seq[0]:
                    boxes[box][i][1] = seq[1]

        else:
            boxesSets[box].add(seq[0])
            boxes[box].append(seq)

ans = 0
for i in range(len(boxes)):
    if not boxes[i]:
        continue
    
    for j in range(len(boxes[i])):
        ans += (i+1)*(j+1)*int(boxes[i][j][1])

print(ans)