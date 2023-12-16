def constructHistory(line):
    #Recursively constructs the history 
    newLine = []
    for i in range(len(line) - 1):
        newLine.append(line[i+1] - line[i])
    if not any(newLine):
        return [newLine]
    else:
        return [newLine] + constructHistory(newLine)
    
def nextValue(history):
    #Predicts the next value given a history
    sum = 0
    for hist in history[::-1]:
        sum += hist[-1]
    return sum

with open('g:/Programmering/Python/Advent of code/Day 9/input.txt', 'r') as file:
    histories = []
    ans = 0
    for line in file:
        line = [int(x) for x in line.strip().split()][::-1]
        ans += nextValue([line] + constructHistory(line))   

print(ans)